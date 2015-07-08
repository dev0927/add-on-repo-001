
import sys
import xbmcgui
import xbmcplugin

def config_channel(encoded_name,encoded_url):
	name = encoded_name.decode('base64')
	url = encoded_url.decode('base64')
	li = xbmcgui.ListItem(name, iconImage='DefaultVideo.png')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

name='SEJPMkVhc3RIRA=='
url = 'aHR0cDovLzMxLjIyMC40MS4xMTE6ODAvTGl2ZUVkZ2UvSEJPMkVhc3RIRC9wbGF5bGlzdC5tM3U4P3Rva2VuPTVlMTEzZTYzMjdmOGU5MTU5OGU5NGUxNjYwODZlZDVj'
config_channel(name, url)
name='VklFVC1TRVg='
url = 'cnRtcDovLzY0LjYyLjE0My41L2xpdmUvZG8lMjBub3QlMjBzdGVhbCUyMG15LVN0cmVhbTI='
config_channel(name, url)
name='Rk0gMTA1IQ=='
url = 'cnRtcDovL2Ztcy4xMDUubmV0OjE5MzUvbGl2ZSBwbGF5cGF0aD0xMDVUZXN0MSBsaXZlPXRydWU='
config_channel(name, url)
name='QlJBWlpFUlMgRVVST1BF'
url = 'aHR0cDovLzIxMi4yMjAuMzAuMjE5L2hscy9DSF9CUkFaWkVSU1RWL2J3MTUwMDAwMC92YXJpYW50Lm0zdTg/dmVyc2lvbj0y'
config_channel(name, url)
name='UExBWUJPWQ=='
url = 'aHR0cDovLzIxMi4yMjAuMzAuMjE5L2hscy9DSF9QTEFZQk9ZL2J3MTUwMDAwMC92YXJpYW50Lm0zdTg/dmVyc2lvbj0y'
config_channel(name, url)
name='WFhM'
url = 'aHR0cDovLzIxMi4yMjAuMzAuMjE5L2hscy9DSF9YWEwvYncxNTAwMDAwL3ZhcmlhbnQubTN1OD92ZXJzaW9uPTI='
config_channel(name, url)
name='QkxVRSBIVVNUTEVS'
url = 'aHR0cDovLzIxMi4yMjAuMzAuMjE5L2hscy9DSF9CTFVFSFVTVExFUi9idzE1MDAwMDAvdmFyaWFudC5tM3U4P3ZlcnNpb249Mg=='
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVA=='
url = 'aHR0cDovLzIxMi4yMjAuMzAuMjE5L2hscy9DSF9SVVNTSUFOTklHSFQvYncxNTAwMDAwL3ZhcmlhbnQubTN1OD92ZXJzaW9uPTI='
config_channel(name, url)
name='T0xBTEE='
url = 'aHR0cDovLzIxMi4yMjAuMzAuMjE5L2hscy9DSF9PTEFMQS9idzE1MDAwMDAvdmFyaWFudC5tM3U4P3ZlcnNpb249Mg=='
config_channel(name, url)
name='TWlhbWkgVFY='
url = 'aHR0cDovL2s0LnVzYXN0cmVhbXMuY29tOjE5MzUvbWlhbWl0di9zbWlsOm1pYW1pdHYvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='UGFzc2llWFhY'
url = 'cnRtcDovLzE3OC4zMy4xMjYuMjEzL2xldmVkLyBwbGF5UGF0aD1wYXNzaWVsaXZlc3RyZWFtIHN3ZlVybD1odHRwczovL3N0YXRpYy5yYW1wYW50LnR2L3N3Zi9wbGF5ZXIuc3dm'
config_channel(name, url)
name='UHJpdmF0ZQ=='
url = 'aHR0cDovLzE3OC4zMy4xMjYuMjEzOjE5MzUvbGV2ZWQvcHJpdmF0ZUNvbS8ubTN1OA=='
config_channel(name, url)


xbmcplugin.endOfDirectory(addon_handle)