import os
import re
import sys
'''
import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin
'''
import urllib, urllib2
from HTMLParser import HTMLParser

def open_url(url, referer=None, data=None): #add optional headers ...  

    response = urllib2.urlopen(url)
    page = response.read()
    response.close()
    return page


class Chaturbate(object):
    debug = False
    _REGEX_media = re.compile(r"initHlsPlayer\(jsplayer, '(.*?)\?rp\=")
    BASE_URL        = "https://chaturbate.com"
    CATEGORY_URL    = {
        "Featured":     BASE_URL,
        "Female":       BASE_URL + "/female-cams/",
        "Male":         BASE_URL + "/male-cams/",
        "Couple":       BASE_URL + "/couple-cams/",
        "Transsexual":  BASE_URL + "/trans-cams/"
    }
    def __init__(self):
        self._last_page = False
    
    def get_categories(self):
        list = []
        for key in self.CATEGORY_URL:
            list.append(key)
        return list    
    
    def on_last_page(self):
        return self._last_page
    
    def _get_models_on_page(self, category="Featured", page=None): 
        if(page == None):
            url = self.CATEGORY_URL[category]
        else:
            url = self.CATEGORY_URL[category] + "?page=" + str(page)
        p = ModelListParser(debug=self.debug)
        p.reset()
        response = open_url(url)
        try:
            p.feed(response.decode("UTF-8"))
        except UnicodeDecodeError:
            print response    
        except Exception as e:
            print e.__class__.__name__ + ':' 
            print e
            '''
            if (e.errno):
                print "Error({0}): {1}".format(e.errno, e.strerror)            #output page
                print(response)
            else:
                print e
            '''
        self._last_page = p.is_last_page()    
        return p.models
    
    def get_model_media(self, model):
        #TODO check if 'media' exists first
        url = None
        page = open_url(self.BASE_URL + '/' + model + '/')
        data = self._REGEX_media.findall(page)
        for x in data:
            url = x
        return url    
class ModelParser(HTMLParser):
 
    def __init__(self):
        self.convert_charrefs = True
        self.cdata_elem = None
        self.strict = False
        
    def handle_starttag(self, tag, attrs):
        return
    def handle_endtag(self, tag):
        return ""
    def handle_data(self, data):
        return ""
    
class ModelListParser(HTMLParser):
 
    def __init__(self, debug=True):
        self.convert_charrefs = True
        self.cdata_elem = None
        self.strict = False
        self._debug = debug
        
        self.pagingInfoStarted = False
        self._last_page = False
        self.processingModel = False
        self.subjectStarted = False
        self.subInfoStarted = False
        self.listFound = False
        self.modelDetailsFound = False
        self.modelTitleFound = False
        self.subjectTitleFound = False
        self.camsViewerDataFound = False
        self.sQualityInfoFound = False
        self.locationDataFound = False
        self.imageAnchorLocated = False
        self.titleAnchorFound = False
        self.skipRest = False
        self.currentModel = None
        self.models = []
    
    def debug(self, text):
        if(self._debug == True):
            print text
    
    def is_last_page(self):
        return self._last_page
    
    def handle_starttag(self, tag, attrs):
        # self.debug('start ' + tag)
         #print tag
         #print len(attrs)
         if(self.skipRest == True):
             return    
         if(tag == 'ul'):
            for attr in attrs:
                #self.debug( attr  ('id','nav') )
                if(attr[0]=="class" and attr[1] == "list"):
                    self.debug( "Model List Started" )
                    self.listFound = True
                elif(attr[0]=="class" and attr[1] == "subject"):
                    #part of model entry
                    self.subjectStarted = True
                    self.debug( "Start of Subject" )
                elif(attr[0] == "class" and attr[1] == 'sub-info'):
                    self.subInfoStarted = True
                    self.debug( "Start of Sub Info")
                elif(attr[0] == "class" and attr[1] == 'paging'):
                    self.pagingInfoStarted = True
                
         elif(tag == 'li'):
            if(len(attrs) < 1):
                if(self.listFound == True):
                    #start new model entry
                    self.processingModel = True
                    self.currentModel = {}  #new tuple or dict here
                    self.debug( "Start of Model" )
                elif(self.pagingInfoStarted):
                    return  #ignore for now until processing  TODO process page to get current and last pages  
                else:
                    self.debug( "Unexpected condition" )
            else:
                for attr in attrs:
                    if(attr[0] == "title" and self.subjectStarted):
                        self.debug( "Subject Title")
                        self.debug((attr[1]))
                        self.subjectTitleFound = True
                    if(attr[0] == "class" and attr[1] == "location"):
                        self.locationDataFound = True
                    if(attr[0] == "class" and attr[1] == "cams"):
                        self.camsViewerDataFound = True
         elif(tag == 'a'):
            if(self.processingModel == True and self.modelDetailsFound == False):
                for attr in attrs:
                    if(attr[0] == 'href'):
                        self.currentModel['url'] = attr[1]
                        self.imageAnchorLocated = True
                #use this to get the image loc and url
                self.modelImgDataFound = True #may need more info
            elif(self.modelTitleFound == True):
                #used for locating span
                self.titleAnchorFound = True
            elif(self.pagingInfoStarted == True):
                _next = False
                _hash = False
                for attr in attrs:
                    if(attr[0] == 'class'):
                        if('next' in attr[1]):
                            self.debug( "next element found" )
                            _next = True
                    elif(attr[0] == 'href' and attr[1] == '#'):
                        self.debug( "hash found" )
                        _hash = True
                self.debug("hash:" + str(_hash))
                self.debug("next:" + str(_next))        
                if(_next == True and _hash == True):
                    self.debug( "Last page found" )
                    self._last_page = True
         elif(tag == 'div'):
             for attr in attrs:
                 if (attr[0] == 'class' and attr[1] == 'details'):
                     self.modelDetailsFound = True
                 elif(attr[0] == 'class' and attr[1] == 'title'):
                     self.modelTitleFound = True
                 elif(attr[0] == 'class' and 'thumbnail_label' in attr[1]):
                     self.sQualityInfoFound = True
         elif(tag == 'img'):
             if(self.imageAnchorLocated == True):
                 for attr in attrs:
                     #check if in a
                     if(attr[0] == 'src'):
                         self.debug( attr[1] )
                         self.currentModel['image']= attr[1]
                 self.imageAnchorLocated = False        
    def handle_endtag(self, tag):
        if(self.skipRest == True):
             return    
#        self.debug('end ' + tag)
        if(tag == 'ul'):
            if(self.subjectStarted == True):
                self.debug( "End Subject" )
                self.subjectStarted = False
            
            elif(self.subInfoStarted == True):
                self.debug( "End Sub Info" )
                self.subInfoStarted = False
            elif (self.listFound == True):
                if(self.processingModel == True):
                    self.debug( "End of subject" )
                else:
                    self.listFound = False
                    self.debug( "End of model list" )
            elif(self.pagingInfoStarted == True):
                self.pagingInfoStarted = False
                self.skipRest = True
                self.debug( "End of Paging Section" )
        elif(tag == 'li'):
            if(self.locationDataFound == True):
                self.locationDataFound = False
            elif(self.camsViewerDataFound == True):
                self.camsViewerDataFound = False
            elif(self.subjectTitleFound == True):
                self.debug( "End of Subject Title" )
                self.subjectTitleFound = False
            elif( self.listFound == True and self.processingModel == True):
                self.debug( "End of Model" )
                #put currentModel into array
                self.models.append(self.currentModel)
                self.processingModel = False
                self.currentModel = None
        elif (tag == 'a'):
            if(self.titleAnchorFound == True):
                self.titleAnchorFound = False        
        elif(tag == 'div'):
            if(self.modelTitleFound == True):
                #clear the div
                self.modelTitleFound = False
                self.debug( "End of Model Title" )
            elif(self.modelDetailsFound == True):
                #clear the details
                self.modelDetailsFound = False
                self.debug( "End of Details" )
            elif(self.sQualityInfoFound == True):
                self.debug( "End of StreamDefInfo" )
                self.sQualityInfoFound = False    
            else:
                self.debug("missed a div!!!!")
    def handle_data(self, data):
        if(self.skipRest == True):
             return    
        if(self.titleAnchorFound == True):
            self.currentModel['name'] = data.strip()
            self.debug('data: %s' % (data))
        if(self.locationDataFound):
            self.debug('location: %s' % (data))
        if(self.sQualityInfoFound == True):
            self.debug( data )
            
if __name__ == "__main__":
    Chaturbate()
                