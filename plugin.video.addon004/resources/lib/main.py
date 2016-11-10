import sys, urllib, urllib2,re
from urlparse import parse_qsl

import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]

# Get the plugin handle as an integer number.
addon_handle = int(sys.argv[1])


#TODO parse _url for params????


#TODO Add singly now but would be more efficient to add all at once with addDirectoryItems instead reconfigure how items identified/stored See example plugin 
def add(sUrl, resolver=None, name=None, thumb=None, fanArt=None, title=None):
         # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4

    if name: 
        label = name
    else:
        label = sUrl.upper()
        
    url = '{0}?action=play&resolver={2}&video={1}'.format(_url, sUrl, resolver)
   
    # Create a list item with a text label 
    list_item = xbmcgui.ListItem(label=label)
    #TODO Finish the extra bells and whistles
    '''        
    # Set a fanart image for the list item.
    # Here we use the same image as the thumbnail for simplicity's sake.
    list_item.setProperty('fanart_image', video['thumb'])
    # Set additional info for the list item.
    list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
    # Set additional graphics (banner, poster, landscape etc.) for the list item.
    # Again, here we use the same image as the thumbnail for simplicity's sake.
    list_item.setArt({'landscape': video['thumb']})
    # Set 'IsPlayable' property to 'true'.
    # This is mandatory for playable items!
    list_item.setProperty('IsPlayable', 'true')
    # Create a URL for the plugin recursive callback.
    # Add the list item to a virtual Kodi folder.
    # is_folder = False means that this item won't open any sub-list.
    is_folder = False
    '''
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item)


def play(name,streamurl,iconimage = "DefaultVideo.png"):
    #streamurl += ' timeout=15'
    liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
    '''
    liz.setInfo('video', {'Title': name })
    liz.setProperty('IsPlayable', 'true')
    liz.setPath(path=streamurl)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]),True,liz)
    '''
    player = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    player.play(streamurl,liz)
    
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

def getUrl(url):
    opener = urllib2.build_opener(NoRedirectHandler()) 
    
    req = urllib2.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0')
    req.add_header("Connection", "keep-alive")
    req.add_header("Referer", url)
    #open initial page
    response = opener.open(req)
    page = response.read()
    return page

class streamin:
    def info(self):
        return {
            'netloc': ['streamin.to'],
            'host': ['Streamin'],
            'quality': 'Medium',
            'captcha': False,
            'a/c': False
        }

    def resolve(self, url):

            url = 'http://streamin.to/embed-%s.html' % url

            result = getUrl(url)
            url = re.compile("file *: *[\'|\"](http.+?)[\'|\"]").findall(result)[-1]
            return url
    
def create_list():    
    xbmcplugin.setContent(addon_handle, 'movies')
    
    ## add channels
    add('pxpbrxk78xq0','streamin')
    add('omjj0oin3wxh','streamin')
    add('3wx0v8gw58rq','streamin')
    add('dz133vwiw3tw','streamin')
    add('wskvm9jy8un6','streamin')
    add('v6o8a5lefiz8','streamin')
    add('ewz8562gwn5u','streamin')
    add('45l6ydfshaa8','streamin')
    add('wev7k53oinwb','streamin')
    add('o4zekwta7mm8','streamin')
    add('t8uhenkdrfoz','streamin')
    add('8rd620xq36g2','streamin')
    add('xosvknv5vsqs','streamin')
    add('igj8xovyr0ww','streamin')
    add('46aeueun2xlx','streamin')
    add('ek9jiefibmma','streamin')
    add('indx0gp0euwq','streamin')
    add('br7mmveg6d7q','streamin')
    add('0njmibpeu6nh','streamin')
    add('2f0szsa9u0eo','streamin')
    add('oyz2d9vnwpo8','streamin')
    add('lq0atd308oyl','streamin')
    add('bjece95vvggw','streamin')
    add('4uqbev88i0gn','streamin')
    add('ob7yr3xrf4iz','streamin')
    add('80r4ucl8a9em','streamin')
    add('9amri1bwpueg','streamin')
    add('bhjpu4wu30f3','streamin')
    add('bhjk4tbppufp','streamin')
    add('zzk710y92yn0','streamin')
    add('re66uqiekzhy','streamin')
    add('q2itgvz34inp','streamin')
    add('ek29c9pm2xar','streamin')
    add('1smj73fkf8v7','streamin')
    add('jcjj2wf7bzy2','streamin')
    add('kcdrpyr0xf6y','streamin')
    add('xhzxfb0v7wce','streamin')
    add('z2uiw3dxscf8','streamin')
    add('cam78oyl6myk','streamin')
    add('6dzjeiiwk5dp','streamin')
    add('ti780dw09rds','streamin')
    add('j679qeur7h02','streamin')
    add('kfpk073see63','streamin')
    add('ixjzwzifj277','streamin')
    add('nr76a9meycj8','streamin')
    add('tdwzqwqlkylw','streamin')
    add('9e2concohtme','streamin')
    add('qyi2ojm1ps7s','streamin')
    add('8gj0crm3bimd','streamin')
    add('ed5vv281e2dv','streamin')
    add('0y69cfm13ocu','streamin')
    add('45pb6kljlg4m','streamin')
    add('otl4zada9fvf','streamin')
    add('02z8uxk9bgda','streamin')
    add('7a6vh9exdzlx','streamin')
    add('7t4bh6fd5913','streamin')
    add('hpo5919fv3z3','streamin')
    add('dapm2lvgl9s5','streamin')
    add('e6v5vor13518','streamin')
    add('kmzqkzdyy84t','streamin')
    add('t36wk2uxbj2p','streamin')
    add('5fighkr6etuh','streamin')
    add('z8hk7m7qo31u','streamin')
    add('xz3hauwko3c8','streamin')
    add('663q2wsg2x8q','streamin')
    add('23iw7b807kij','streamin')
    add('ndmt59nno8iv','streamin')
    add('yjsy6mimkchw','streamin')
    add('kodt7fu3xez0','streamin')
    add('04fj79pl2r8i','streamin')
    add('y9qxfavzpmi4','streamin')
    add('v4pjg1295z8q','streamin')
    add('3ugr41xg9m10','streamin')
    add('396y1dfpvyq0','streamin')
    add('lerj7yhibt5f','streamin')
    add('4zo3rkic5w7e','streamin')
    add('kr9eltqn1mzv','streamin')
    add('dls2mr6ggtd2','streamin')
    add('hmy9k4ygt1tl','streamin')

    xbmcplugin.endOfDirectory(addon_handle)
def test_resolve():
    print streamin().resolve('xz3hauwko3c8')

def router(paramstring):
    
        # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))

    # Check the parameters passed to the plugin
    if params:
        url = params['video']
        if params['action'] == 'play':
            # Play a video from a provided URL.
            if params['resolver']!= None and params['resolver']!='None':
                url = globals()[params['resolver']]().resolve(url)
            play('name',url)
        #elif params['action'] == 'listing':
                #For future *pages*
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of videos
        create_list()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])

