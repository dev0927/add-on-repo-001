
import sys,io,json,os
import urllib, urllib2, hashlib
from urlparse import parse_qsl

import xbmc, xbmcgui, xbmcplugin, xbmcaddon

## a flat single directory style plugin
AddonID = 'plugin.video.addon001'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")

resourceDir = os.path.join(addonDir, 'resources')

addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

class SmartRedirectHandler(urllib2.HTTPRedirectHandler):
	def http_error_301(self, req, fp, code, msg, headers):
		result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
		return result

	def http_error_302(self, req, fp, code, msg, headers):
		result = urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
		return result

def getFinalUrl(url):
	link = url
	try:
		req = urllib2.Request(url) 
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')
		opener = urllib2.build_opener(SmartRedirectHandler())
		f = opener.open(req)
		link = f.url
		if link is None or link == '':
			link = url
	except Exception as ex:
		xbmc.log(str(ex), 3)
	return link	

def config_channel(encoded_name, encoded_url):
	name = encoded_name.decode('base64')
	li = xbmcgui.ListItem(name, iconImage='DefaultVideo.png')
	urlParams = {'stream': encoded_url, 'mode': 'play', 'name': name}
	u = '{0}?{1}'.format(sys.argv[0], urllib.urlencode(urlParams))
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=u, listitem=li)
def processPlaylist():
	with open(os.path.join(resourceDir,"playlist")) as f:
		content = json.load(f)
	
	for channel in content:
		config_channel(channel["name"],channel["url"])
	xbmcplugin.endOfDirectory(addon_handle)

def play(name, stream):
	url = stream.decode('base64')
	xbmc.log('--- Finalizing "{0}". {1}'.format(name, url), 2)
	url = getFinalUrl(url)
	print '--- Playing "{0}". {1}'.format(name, url)
	xbmc.log('--- Playing "{0}". {1}'.format(name, url), 2)
#	url = getFinalUrl(stream.decode("base64"))
	liz = xbmcgui.ListItem(name)
	player = xbmc.Player()
	player.play(url,liz)

def router(paramstring):

    params = dict(parse_qsl(paramstring))

    # Check the parameters passed to the plugin
    if params:
        if 'mode' in params and params['mode']!= None and params['mode']!='None':
            if params['mode'] == 'play':
                play(params['name'],params['stream'])
    else:
        processPlaylist()


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
