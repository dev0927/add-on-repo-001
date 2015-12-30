import urllib,urllib2, re,base64, time, math
from HTMLParser import HTMLParser

def get_src(word, txt):
    regexpstr = word + "'?[ :=]+['\"]?([^ ',\"]+)" 
    src = re.compile(regexpstr).findall(txt)[0]
    return src

def unescape(src, byteSize=32):
    if(byteSize == 32):
        return re.sub(r'%([a-fA-F0-9]{2})', lambda m: chr(int(m.group(1), 16)), src)
    else:
        return re.sub(r'%([a-fA-F0-9]{4}|[a-fA-F0-9]{2})', lambda m: chr(int(m.group(1), 16)), src)

class NoRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        infourl = urllib.addinfourl(fp, headers, req.get_full_url())
        infourl.status = code
        infourl.code = code
        return infourl
    http_error_300 = http_error_302
    http_error_301 = http_error_302
    http_error_303 = http_error_302
    http_error_307 = http_error_302

class VerdirectoParser(HTMLParser):    
    def __init__(self):
        self.convert_charrefs = True
        self.cdata_elem = None
        self.strict = False
        self.script_url = None

    def handle_starttag(self, tag, attrs):
        if(tag == 'script'):
            #process
            for attr in attrs:
                if(attr[0]=="src"):
                    #print(attr[1])
                    if(len(re.findall("verdirectotv.org", attr[1])) > 0):
                        #print("Found script url: " + attr[1])
                        self.script_url = attr[1]

    def get_script_url(self):
        return self.script_url
    def has_script_url(self):
        return self.script_url != None
    
class IFrameSrcParser(HTMLParser):
    def __init__(self):
        self.convert_charrefs = True
        self.cdata_elem = None
        self.strict = False
        self.src = ()
    def handle_starttag(self, tag, attrs):
        if(tag == "iframe"):
            for attr in attrs:
                if(attr[0]=="src"):
                    #add to list instead of overwrite // let caller choose from multiples
                    self.src = self.src + (attr[1],)
    def get_src(self):
        return self.src
    def match(self, src, text):
        return text in src

class HiddenInputParser(HTMLParser):
    
    def __init__(self):
        self.convert_charrefs = True
        self.cdata_elem = None
        self.strict = False
        self.inputs = ()
    def handle_starttag(self, tag, attrs):
        if(tag == "input"):
            _input = {}
            for attr in attrs:
                #use proper python hash
                _input[attr[0]]=attr[1]
            #probably not necessary but keeping to the name of the class
            if("type" in _input and _input["type"]=="hidden"):
                self.inputs = self.inputs + (_input,)
    def getInput(self, _id):
        for _input in self.inputs:
            if('id' in _input and _input['id'] == _id):
                return _input    
        
def pbr_resolver(url):
    opener = urllib2.build_opener(NoRedirectHandler()) 
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
    req.add_header("Connection", "keep-alive")
    req.add_header("Referer", url)
	#open initial page
    response = opener.open(req)
    page = response.read()
    ####diag
    print '====' + url + "==========="
    print page
    ###diag#end
    return _resolve(page, url, opener)

def _resolve(page, url, opener):
	#get/request next embed step
    p =  IFrameSrcParser()
    p.reset()
    p.feed(str(page))

    pageUrl = p.get_src()
    if(len(pageUrl)>1) :
        #check if url matches current url
        for i in pageUrl:
            if(i != url and (p.match(i,"verdirectotv") or p.match(i,"cinestrenostv")) ) :
            #if(i != url ) :
                pageUrl = i
    else :
        pageUrl = pageUrl[0]
    print('====' + pageUrl + '========')
    req = urllib2.Request(pageUrl)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
    req.add_header("Connection", "keep-alive")
    req.add_header("Referer", url)
    
    response = opener.open(req)

    page=response.read()
    
    print(page)
    
    p = VerdirectoParser()
    p.reset()
    p.feed(str(page))
    
    if(p.has_script_url()):
        sUrl = p.get_script_url()
        req = urllib2.Request(sUrl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
        req.add_header("Connection", "keep-alive")
        req.add_header("Referer", pageUrl)
        response = opener.open(req)
        page=response.read()
        p =  IFrameSrcParser()
        p.reset()
        p.feed(str(page))

        pageUrl = p.get_src()
        if(len(pageUrl)>1) :
            #check if url matches current url
            for i in pageUrl:
                if(i != url) :
                    pageUrl = i
        else :
            pageUrl = pageUrl[0]
        req = urllib2.Request(pageUrl)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
        req.add_header("Connection", "keep-alive")
        req.add_header("Referer", sUrl)
        
        response = opener.open(req)
        embed=response.read()
        
        embed = embed.decode('utf-8')
        iParser = HiddenInputParser()
        iParser.reset()
        iParser.feed(embed)
        if(len(iParser.inputs) > 0):
        #seems to swap between these two methods not sure of when switch happens ie weekend/weekday etc
            return get_stream_parameters(embed, iParser, pageUrl)
        else:
            return get_stream_parameters_remote(opener, embed, pageUrl)
    else:
        return _resolve(page, pageUrl, opener)
        ##TODO drill down until we get a script we are looking for

## it seams the page alternates between this and the other signature (not sure when/why)
def get_stream_parameters_remote(opener, src, referer=None):    
    ## this iteration of the website had included a call to get the path from a third party
    ## this appears to be no longer part of the design but keeping in case these changes are cyclical
    ## it was never tested as the web site design changed just before testing!!!
    #get the variable name from the embed script/html
    cod = ()
    regexpstr = "v_cod1: ([a-zA-Z0-9=\-_]+)" 
    result = re.findall(regexpstr, src)
    for r in result:
        if(r != "cod1"):
            cod += (r,) 
            #print(r)
    regexpstr = "v_cod2: ([a-zA-Z0-9=\-_]+)" 
    result = re.findall(regexpstr, src)
    for r in result:
        if(r != "cod2"):
            cod += (r,) 
            #print(r)
    #as it is now 'url' is only used once on page but may need to be more specific as it is a common var name
    regexpstr = "url: ([a-zA-Z0-9=\-_]+)" 
    result = re.findall(regexpstr, src)
    for r in result:
        if(r != "sUrl"):
            cod += (r,) 
            #print(r)
    
    result = cod

    # now find the actual base64 data needed to send
    regexpstr = "var " + result[0] + " = \"([a-zA-Z0-9=\+\-/_ ]+)\""
    v_cod1 = re.findall(regexpstr, src)[0]
    regexpstr = "var " + result[1] + " = \"([a-zA-Z0-9=\+\-/_ ]+)\""
    v_cod2 = re.findall(regexpstr, src)[0]
    regexpstr = "var " + result[2] + " = \"([a-zA-Z0-9=\+\-/_ ]+)\""
    zUrl = re.findall(regexpstr, src)[0]
    zUrl = base64.b64decode(zUrl).decode('utf-8')
    _ts = time.time() 
    t = int( math.floor( _ts * 1000 ) )
    #todo should randomize the callback name somewhat as jQuery might be doing
    zUrl = zUrl + "?callback=jQuery1706832507512518498_" + str(t) + "&v_cod1="  + urllib.quote_plus(v_cod1) + "&v_cod2=" + urllib.quote_plus(v_cod2) + "&_=" + str(t + 30)
    if(opener==None):
        opener = urllib2.build_opener(NoRedirectHandler()) 
    req = urllib2.Request(zUrl)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
    req.add_header("Connection", "keep-alive")
#    req.add_header("Referer", referer)
    response = opener.open(req)
    src = response.read()
    src = src.decode('utf-8');
    ##parse response for the data we need for the stream
    regexpstr = r"streamer: '([0-9a-zA-z.:/?=@]+)'"
    streamer = re.findall(regexpstr, src)[0]
    streamer = re.sub(r"\\","", streamer)
    regexpstr = r"rtmpe?:\/\/[0-9.:/]+(.+)"
    app = re.findall(regexpstr, streamer)[0]
    regexpstr = "file: '([0-9a-zA-z.:/?=@]+)'"
    _file = re.findall(regexpstr, src)[0]
    _file = re.sub(r"\\","", _file)

    ##kodi style
    kodistream = streamer + " playpath=" + _file +  " swfUrl=http://www.businessapp1.pw/jwplayer5/addplayer/jwplayer.flash.swf pageUrl=" + referer + " app=" + app + " flashVer=\"LNX 10,0,32,18\"" 
    return kodistream
    
def get_stream_parameters(src, iParser, pageUrl):    
    #this is almost back to the first design except that some code is 'encoded' in escaped text
    #get the variable name from the embed script/html
    #For this design it we need to search hidden fields for the base64 data
    #The correlation is:
    #        XAF1 ==> sx1 ==> d_sx1 ==> result1 ==> 'file'
    #        GADA ==> sx2 ==> d_sx2 ==> result2 ==> 'streamer'
    # Doesn't appear to be necessary to decode the escaped data each time (but that could change)
    
    regexpstr = "XAAF1  = document.getElementById\((.*?)\)"
    result = re.findall(regexpstr, src)
    if(len(result)>0):
        XAF1 = re.findall("([a-zA-Z0-9=\+\-/_ ]+)", result[0])[0]
    else:
        regexpstr = "XAF1  = document.getElementById\((.*?)\)"
        result = re.findall(regexpstr, src)[0]
        #strip the single quotes also ensure base64 but this is not strictly checked
        XAF1 = re.findall("([a-zA-Z0-9=\+\-/_ ]+)", result)[0]
    
    regexpstr = "GAADA  = document.getElementById\((.*?)\)"
    result = re.findall(regexpstr, src)
    if(len(result)>0):
        GADA = re.findall("([a-zA-Z0-9=\+\-/_ ]+)", result[0])[0]
    else:
        regexpstr = "GADA  = document.getElementById\((.*?)\)"
        result = re.findall(regexpstr, src)[0]
        #strip the single quotes also ensure base64 but this is not strictly checked
        GADA = re.findall("([a-zA-Z0-9=\+\-/_ ]+)", result)[0]
    
    _file  = base64.b64decode(iParser.getInput(XAF1)["value"]).decode('utf-8')
    streamer = base64.b64decode(iParser.getInput(GADA)["value"]).decode('utf-8')

    regexpstr = r"rtmpe?:\/\/[0-9.:/]+(.+)"
    app = re.findall(regexpstr, streamer)[0]
    ##kodi style
    kodistream = streamer + " playpath=" + _file +  " swfUrl=http://www.businessapp1.pw/jwplayer5/addplayer/jwplayer.flash.swf pageUrl=" + pageUrl 
   
    return kodistream
   

print(pbr_resolver("http://cinestrenostv.tv/canales/nacionales/hustlertv.php"))
#print(pbr_resolver("http://verdirectotv.com/canales/hustlertv.html"))
#print(pbr_resolver("http://verdirectotv.com/tv/xxx2/playboy.html"))
#print(pbr_resolver("http://cinestrenostv.tv/canales/emision/hustlertv.html"))
#print(pbr_resolverkk("http://cinestrenostv.tv/canales/nacionales/hustlertv.php"))