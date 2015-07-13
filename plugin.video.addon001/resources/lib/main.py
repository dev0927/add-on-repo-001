
import sys
import xbmcgui
import xbmcplugin

def config_channel(encoded_name,encoded_url, video=None, audio=None, subtitle=None):
	name = encoded_name.decode('base64')
	url = encoded_url.decode('base64')
	li = xbmcgui.ListItem(name, iconImage='DefaultVideo.png')
	if(info):
		li.addStreamInfo('video', video, audio)
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

name='VEVTVA=='
url = 'aHR0cDovLzE5OS4xOTUuMTk1LjEwODozMjAwNQ=='
config_channel(name, url,{ 'codec': 'h264', 'width': 720,'height': 418, 'duration': 60 },{'codec': 'mp4a', 'channels':2})
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
name='VmVudXM='
url = 'cnRtcDovLzUwLjcuMjguMTYyL2FwcCBwbGF5cGF0aD0xNjgxMz9NVFF6TmpVMk1qY3hORHN4WlRnd01EWTBOak5sWkRFek1HVXlPVGMzTWpSa04yWTJaR1F5TkdWak1nPT0gc3dmVXJsPWh0dHA6Ly9jZG4uc2hpZHVybGl2ZS5jb20vcGxheWVyLnN3ZiBwYWdlVXJsPWh0dHA6Ly93d3cuc2hpZHVybGl2ZS5jb20vc3RyZWFtLzRlN2E1MTMzNGU1NDYzMzA0ZTdhNTkzMzRlNmE1OTMxNGU2ZDU1MzM0ZTU0NjQ2OC9jZjQ5ZWQ1ZWY2ZWE='
config_channel(name, url)
name='U2V4dHJlbWU='
url = 'cnRtcDovLzUwLjcuMjguODIvYXBwIHBsYXlwYXRoPTE2OTcxP01UUXpOalUyTXpBd01qc3pNREE1TldJNFptTXpObU16TW1ReU1qRmlORFZsTVdVMU16SmtaakpoT0E9PSBzd2ZVcmw9aHR0cDovL2Nkbi5zaGlkdXJsaXZlLmNvbS9wbGF5ZXIuc3dmIHBhZ2VVcmw9aHR0cDovL3d3dy5zaGlkdXJsaXZlLmNvbS9zdHJlYW0vNGU3YTUxMzM0ZTU0NjMzMDRlN2E1OTMzNGQ0NDYzNzk0ZTZhNmIzMzRlNmE1OTc4NGU2YTUxMzI1YTY3M2QzZC82NWVmYWVhMTk1Njg='
config_channel(name, url)



xbmcplugin.endOfDirectory(addon_handle)