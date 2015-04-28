
import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'rtmp://fms.105.net:1935/live playpath=105Test1 live=true'
li = xbmcgui.ListItem('FM 105!', iconImage='DefaultVideo.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)