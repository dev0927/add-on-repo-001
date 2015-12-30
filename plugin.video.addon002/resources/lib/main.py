
import sys
import xbmcgui
import xbmcplugin
import html_list_resolver

def config_channel(encoded_name,encoded_url, video=None, audio=None, subtitle=None, icon=None):
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
	
addon_handle = int(sys.argv[1])

## put up waiting dialog

html_list_resolver.item_resolver('aHR0cDovL2hkZnVsbGhkLmV1L0FEVUxULnR4dA==')

xbmcplugin.setContent(addon_handle, 'movies')



xbmcplugin.endOfDirectory(addon_handle)