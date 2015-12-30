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

def item_resolver(encoded_url):
    opener = urllib2.build_opener(NoRedirectHandler()) 
    url = encoded_url.decode('base64')
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
    req.add_header("Connection", "keep-alive")
    req.add_header("Referer", url)
	#open initial page
    response = opener.open(req)
    page = response.read()

    items = page.split('\n')
    list = []
    for item in items:
        if (item != ''):
			#split on ,
			data = {}
			values = item.split(',')
		 	data['name']=values[0].encode('base64', 'strict').replace('\n', '')
		 	data['url']=values[1].encode('base64', 'strict').replace('\n', '')
		 	list.append(data)

    return list

#print(item_resolver('aHR0cDovL2hkZnVsbGhkLmV1L0FEVUxULnR4dA=='))
#print(pbr_resolver("http://verdirectotv.com/canales/hustlertv.html"))
#print(pbr_resolver("http://verdirectotv.com/tv/xxx2/playboy.html"))
#print(pbr_resolver("http://cinestrenostv.tv/canales/emision/hustlertv.html"))
#print(pbr_resolverkk("http://cinestrenostv.tv/canales/nacionales/hustlertv.php"))