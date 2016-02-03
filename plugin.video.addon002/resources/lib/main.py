
import sys
import xbmcgui
import xbmcplugin
import html_list_resolver

#simple single list of items

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

def configure_text_channels(encoded_url):
	items = html_list_resolver.item_resolver(encoded_url)
	for item in items:
		config_channel(item['name'], item['url'])
	

def configure_json_channels(encoded_url):
	items = html_list_resolver.item_resolver(encoded_url)
	for item in items:
		config_channel(item['name'], item['url'])
	
	
addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
## put up waiting dialog
#configure_text_channels('aHR0cDovL2hkZnVsbGhkLmV1L0FEVUxULnR4dA==')
configure_json_channels('aHR0cDovL3R2bGlzdC5iaXovdHZ0di9nZXRfbGlzdC5waHA/az1ramFncnV0Z2prdm5ia2FsaA==')


xbmcplugin.endOfDirectory(addon_handle)