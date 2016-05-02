
import sys
import xbmcgui
import xbmcplugin

## a flat single directory style plugin

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
xbmcplugin.setContent(addon_handle, 'movies')

#####################paste links here ##################################################

name='TWlhbWkgVFY='
url = 'aHR0cDovL2s0LnVzYXN0cmVhbXMuY29tOjE5MzUvbWlhbWl0di9zbWlsOm1pYW1pdHYvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='SERQIDE='
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUvNzAvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='SERQIDI='
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUyLzQwL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='UGFzc2llWFhY'
url = 'aHR0cDovLzE3OC40Ni4xNTQuMTA2OjgwMDAvcGxheS9hMDI1'
config_channel(name, url)
name='T0xBTEE='
url = 'aHR0cDovLzRCQTlFQkRCMDdDMDU4ODM6QDUuMTU5Ljk2LjE3MDo4MDAwL29sYWxh'
config_channel(name, url)
name='T0xBTEEgMg=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9vbGFsYQ=='
config_channel(name, url)
name='T0xBTEEgMw=='
url = 'aHR0cDovLzkzLjEwMC4xMDUuMjIxOjQwMjIvdWRwLzIzOS4yMzkuMTMuMTo1MjM5'
config_channel(name, url)
name='QlJBWlpFUlMgRVU='
url = 'aHR0cDovLzRCQTlFQkRCMDdDMDU4ODM6QDUuMTU5Ljk2LjE3MDo4MDAwL2JyYXp6ZXJz'
config_channel(name, url)
name='QlJBWlpFUlMgRVUgMg=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9icmF6emVycw=='
config_channel(name, url)
name='QlJBWlpFUlMgRVUgMw=='
url = 'aHR0cDovLzE3OC40Ni4xNTQuMTA2OjgwMDAvcGxheS9hMDBo'
config_channel(name, url)
name='UExBWUJPWQ=='
url = 'aHR0cDovLzkzLjEwMC4xMDUuMjIxOjQwMjIvdWRwLzIzOS4yMzkuMTMuMjo1MjM5'
config_channel(name, url)
name='UExBWUJPWSAoS1JBUyk='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9wbGF5Ym95'
config_channel(name, url)
name='UExBWUJPWSAz'
url = 'aHR0cDovLzE3OC4zMy4xODIuMTc4OjQ1NTU3L3BsYXkvYTAyaz9hdXRoPXN0cmVhbV90ZXN0XzAwOTg6MkRmZ0Q0NDZ4ekQ4OUZGcnZoaHQ='
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVCA='
url = 'aHR0cDovLzE3OC4zMy4xODIuMTc4OjQ1NTU3L3BsYXkvYTA2cz9hdXRoPXN0cmVhbV90ZXN0XzAwOTg6MkRmZ0Q0NDZ4ekQ4OUZGcnZoaHQ='
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVCAyIChLUkFTKQ=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9ybg=='
config_channel(name, url)
name='TlVBUlQ='
url = 'aHR0cDovLzE3OC4zMy4xODIuMTc4OjQ1NTU3L3BsYXkvYTA0eT9hdXRoPXN0cmVhbV90ZXN0XzAwOTg6MkRmZ0Q0NDZ4ekQ4OUZGcnZoaHQ='
config_channel(name, url)
name='QlVOR0EgQlVOR0E='
url = 'aHR0cDovL2lwdHZmYXN0LmR5bmRucy5vcmc6NTk2OS9saXZlL2Jla2ltL2Jla2ltLzc5My50cw=='
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9odXN0bGVyaGQ='
config_channel(name, url)
name='UEVOVEhPVVNFIEhEIDE='
url = 'aHR0cDovL2Zhc3Ryb290LmRkbnMubmV0OjgwMDAvbGl2ZS9WZW50dXJhL1ZlbnR1cmEvMTEwLnRz'
config_channel(name, url)
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTE0LnRz'
config_channel(name, url)
name='UFJJVkFURSAoRVJPKQ=='
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL243MTYgcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy9oYWxsby10dl9vbmxpbmUv'
config_channel(name, url)
name='RE9SQ0VMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24xODEwIHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcvZG9yY2VsdHZfbGl2ZQ=='
config_channel(name, url)
name='RE9SQ0VM'
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTA2LnRz'
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovL2Zhc3Ryb290LmRkbnMubmV0OjgwMDAvbGl2ZS9WZW50dXJhL1ZlbnR1cmEvMTEzLnRz'
config_channel(name, url)
name='TklHSFQgQ0xVQg=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9uY2x1Yg=='
config_channel(name, url)
name='TmNreXdlaG5l'
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9pc2t1cw=='
config_channel(name, url)
name='RlJFQ0hMT1ZFUg=='
url = 'aHR0cDovLzE3OC40Ni4xNTQuMTA2OjgwMDAvcGxheS9hMDF4'
config_channel(name, url)
name='RlJFQ0hMT1ZFUiAy'
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC43OjEyMzQ='
config_channel(name, url)
name='RlJFQ0hMT1ZFUiAz'
url = 'aHR0cDovLzkzLjEwMC4xMDUuMjIxOjQwMjIvdWRwLzIzOS4yMzkuMTMuNjU6NTIzOQ=='
config_channel(name, url)
name='WFhMKEVSTyk='
url = 'aHR0cDovLzk0LjI1My41Mi4xOTo3Nzg4L3VkcC8yMzQuNS4yLjI0NjoxMjM0'
config_channel(name, url)
name='WFhM'
url = 'aHR0cDovLzk0LjI1My41Mi4xOTo3Nzg4L3VkcC8yMzQuNS4yLjI0NjoxMjM0'
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC44OjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL2Nkbi0wMS5ib251cy10di5ydS9UVkI3L2NhbmR5L3RyYWNrXzBfMzAwMC9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q0FORFkgMg=='
url = 'aHR0cDovLzM3LjIzNS4xNDcuMjUwOjgxL3VkcC8yMjUuNTAuNzAuMToxMjM0'
config_channel(name, url)
name='U0NU'
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTM1LnRz'
config_channel(name, url)
name='RFVTSw=='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTA3LnRz'
config_channel(name, url)
name='TWVpZGVuIHZvbiBIb2xsYW5kIEhhcmQ='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTEyLnRz'
config_channel(name, url)
name='UExBWUJPWSBSRUQ='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTIxLnRz'
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovL2Zhc3Ryb290LmRkbnMubmV0OjgwMDAvbGl2ZS9WZW50dXJhL1ZlbnR1cmEvMTExLnRz'
config_channel(name, url)
name='VkVOVVMgMg=='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTM3LnRz'
config_channel(name, url)
name='WFhYIDE='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTEzLnRz'
config_channel(name, url)
name='WFhYIDI='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTA1LnRz'
config_channel(name, url)
name='WFhYIDM='
url = 'aHR0cDovL2lwdHZnYWZzYS5kZG5zLm5ldDo4MDAwL2xpdmUvYW5kMi9hbmQyLzk1MDMudHM='
config_channel(name, url)
name='SEQgRmFzaGlvbi9OaWdodCBGYW50YXN5'
url = 'aHR0cDovLzE3OC4zMy4xODIuMTc4OjQ1NTU3L3BsYXkvYTAxdT9hdXRoPXN0cmVhbV90ZXN0XzAwOTg6MkRmZ0Q0NDZ4ekQ4OUZGcnZoaHQ='
config_channel(name, url)
name='SE9UIENMVUIgMg=='
url = 'aHR0cDovL2dlbS1hbHRhLWlwdHYubm8taXAubmV0Ojg4OTkvbGl2ZS9iZWxraGlyYWJkb3UxL2JlbGtoaXJhYmRvdTEvNjQzLnRz'
config_channel(name, url)
name='SE9UIENMVUIgMw=='
url = 'aHR0cDovL2dlbS1hbHRhLWlwdHYubm8taXAubmV0Ojg4OTkvbGl2ZS9iZWxraGlyYWJkb3UxL2JlbGtoaXJhYmRvdTEvNjQxLnRz'
config_channel(name, url)
name='SE9UIENMVUIgNA=='
url = 'aHR0cDovL2dlbS1hbHRhLWlwdHYubm8taXAubmV0Ojg4OTkvbGl2ZS9iZWxraGlyYWJkb3UxL2JlbGtoaXJhYmRvdTEvNjQwLnRz'
config_channel(name, url)
name='SE9UIENMVUIgNQ=='
url = 'aHR0cDovL2dlbS1hbHRhLWlwdHYubm8taXAubmV0Ojg4OTkvbGl2ZS9iZWxraGlyYWJkb3UxL2JlbGtoaXJhYmRvdTEvNjM4LnRz'
config_channel(name, url)
name='SE9UIENMVUIgNg=='
url = 'aHR0cDovL2dlbS1hbHRhLWlwdHYubm8taXAubmV0Ojg4OTkvbGl2ZS9iZWxraGlyYWJkb3UxL2JlbGtoaXJhYmRvdTEvNjM3LnRz'
config_channel(name, url)
name='SE9UIENMVUIgNw=='
url = 'aHR0cDovL2dlbS1hbHRhLWlwdHYubm8taXAubmV0Ojg4OTkvbGl2ZS9iZWxraGlyYWJkb3UxL2JlbGtoaXJhYmRvdTEvNjM2LnRz'
config_channel(name, url)
name='SE9UIENMVUIgOA=='
url = 'aHR0cDovL2dlbS1hbHRhLWlwdHYubm8taXAubmV0Ojg4OTkvbGl2ZS9iZWxraGlyYWJkb3UxL2JlbGtoaXJhYmRvdTEvNjM1LnRz'
config_channel(name, url)
name='UlAgMDAx'
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTM2LnRz'
config_channel(name, url)


##############################################################################
xbmcplugin.endOfDirectory(addon_handle)