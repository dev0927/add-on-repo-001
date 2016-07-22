
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

#open file
#readline for name
#readline for url
#repeat until eof
#config channel



name='TWlhbWkgVFY='
url = 'aHR0cDovL2s0LnVzYXN0cmVhbXMuY29tOjE5MzUvbWlhbWl0di9zbWlsOm1pYW1pdHYvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='SERQIDE='
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUvODIvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='SERQIDI='
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUyLzUyL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='U1VQRVJPTkUgSEQ='
url = 'aHR0cDovLzMxLjIyMy4yMzguMTA6ODAwMS8xOjA6MTo0MDk6MjoxOkUwODMxQjM6MDowOjA6'
config_channel(name, url)
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovLzE5NS4yMjguMTEuODk6NDA4MC91ZHAvMjI1LjI1NS4yNTUuNzU6MTAwMDA='
config_channel(name, url)
name='SFVTVExFUiBIRCAoS1JBUyk='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9odXN0bGVyaGQ='
config_channel(name, url)
name='T0xBTEEgKEtSQVMp'
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9vbGFsYQ=='
config_channel(name, url)
name='QlJBWlpFUlMgRVUgKEtSQVMp'
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9icmF6emVycw=='
config_channel(name, url)
name='UExBWUJPWSAoS1JBUyk='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9wbGF5Ym95'
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVCAoS1JBUyk='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9ybg=='
config_channel(name, url)
name='TklHSFQgQ0xVQg=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9uY2x1Yg=='
config_channel(name, url)
name='TmNreXdlaG5l'
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9pc2t1cw=='
config_channel(name, url)
name='QmFsa2FuIEVyb3RpYw=='
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjMyOjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='RXhvdGljYQ=='
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjM0OjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='UExheWhvdXNl'
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjM1OjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='TmV0IFhYTA=='
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjM3OjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='SG90IFBsZWFzdXJl'
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjM4OjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='UHJpdmF0ZQ=='
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjM5OjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='SFVTVExFUiBUVg=='
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjQwOjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjQxOjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='U1VQRVJPTkUgSEQ='
url = 'aHR0cDovLzg5LjIxMi4yNDYuNzM6ODg4OC91ZHAvMjM5LjE4LjIuMjQyOjUwMDA/YXV0aD15ZXM='
config_channel(name, url)
name='UFJJVkFURSAoRVJPKQ=='
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL24xMDI0IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='RE9SQ0VMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24xODEwIHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='WFhMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL242NDgwIHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='T2xhbGEgKEVybyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24yNDggcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='RXVyb3RpYyAoRXJvKQ=='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24xODcgcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='RlJFTkNITE9WRVI='
url = 'aHR0cDovLzkzLjEwMC4xMDUuMjIxOjQwMjIvdWRwLzIzOS4yMzkuMTMuNjU6NTIzOQ=='
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC44OjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL2Nkbi0wMS5ib251cy10di5ydS9UVkI3L2NhbmR5L3RyYWNrXzBfMzAwMC9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='UExBWUJPWSBSRUQ='
url = 'aHR0cDovL2RmMS1wcmVtaWVyZS56YXB0by5vcmc6ODAwMC9saXZlL01hbnVlbC9Db2tlLzM0Ni50cw=='
config_channel(name, url)
name='SlVJQ1k='
url = 'aHR0cDovLzE5OS4xODAuMTE0LjE3NDo4MDAwL2xpdmUvcEhMTmN2OW92MS9WczQ5aGxpTHhpLzgxMy5tM3U4'
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvaGlLUXE5SlpOMy9YYzFic0pxcFU0LzE2NTMudHM='
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovL2RmMS1wcmVtaWVyZS56YXB0by5vcmc6ODAwMC9saXZlL01hbnVlbC9Db2tlLzEwNjgudHM='
config_channel(name, url)
name='U2lyaW5h'
url = 'aHR0cDovL2RmMS1wcmVtaWVyZS56YXB0by5vcmc6ODAwMC9saXZlL01hbnVlbC9Db2tlLzEwNjkudHM='
config_channel(name, url)
name='RG9yY2Vs'
url = 'aHR0cDovL2RmMS1wcmVtaWVyZS56YXB0by5vcmc6ODAwMC9saXZlL01hbnVlbC9Db2tlLzU5OC50cw=='
config_channel(name, url)
name='UElOSyBFUk9USUM='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvaGlLUXE5SlpOMy9YYzFic0pxcFU0Lzc5My50cw=='
config_channel(name, url)
name='UElOSyBFUk9USUMgMg=='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvaGlLUXE5SlpOMy9YYzFic0pxcFU0Lzc5Mi50cw=='
config_channel(name, url)
name='UElOSyBFUk9USUMgMw=='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvaGlLUXE5SlpOMy9YYzFic0pxcFU0Lzc5MS50cw=='
config_channel(name, url)
name='UElOSyBFUk9USUMgNA=='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvaGlLUXE5SlpOMy9YYzFic0pxcFU0Lzc5MC50cw=='
config_channel(name, url)



#############################################################################
xbmcplugin.endOfDirectory(addon_handle)