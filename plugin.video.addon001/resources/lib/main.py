
import sys,io,json,os
import xbmcgui,xbmcplugin,xbmcaddon

## a flat single directory style plugin
AddonID = 'plugin.video.addon001'
Addon = xbmcaddon.Addon(AddonID)
addonDir = Addon.getAddonInfo('path').decode("utf-8")

resourceDir = os.path.join(addonDir, 'resources')
#sys.path.insert(0, libDir)

def config_channel(encoded_name,encoded_url, video=None, audio=None, subtitle=None, icon=None):
	#to_m3u_channel(encoded_name.decode('base64'), encoded_url.decode('base64'))
	#'''
	name = encoded_name.decode('base64')
	url = encoded_url.decode('base64')
	li = xbmcgui.ListItem(name, iconImage='DefaultVideo.png')
	if(video):
		li.addStreamInfo('video', video)
	if(audio):
		li.addStreamInfo('audio', audio)
	if(icon):
		li.setIconImage(icon)
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	#'''
def processPlaylist():
	with open(os.path.join(resourceDir,"playlist")) as f:
		content = json.load(f)
	
	for channel in content:
		config_channel(channel["name"],channel["url"])
	
def playlist_to_m3u():
	
	#TODO deal with path
	with open(os.path.join(resourceDir,"playlist")) as f:
		content = json.load(f)
	
	for channel in content:
		to_m3u_channel(channel["name"].decode("base64"),channel["url"].decode("base64"))
	

def to_m3u_channel(name, url):
	print "#EXTINF:-1, " + name
	print url
	
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

#############################################################################

processPlaylist()
#playlist_to_m3u()

#############################################################################
xbmcplugin.endOfDirectory(addon_handle)