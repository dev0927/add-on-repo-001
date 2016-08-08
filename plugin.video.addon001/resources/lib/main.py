
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
url = 'aHR0cDovLzE3OC4zMy4yMjYuMzY6ODAwMC9saXZlL29sc2kvb2xzaS83OTAudHM='
config_channel(name, url)
name='TmFrZWQgTmV3cw=='
url = 'aHR0cDovLzE3OC4zMy4yMjYuMzY6ODAwMC9saXZlL29sc2kvb2xzaS83OTkudHM='
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
name='T2xhbGEgKEVybyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24yNDggcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='TnVhcnQgKEVybyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24xODcgcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='RlJFTkNITE9WRVI='
url = 'aHR0cDovLzkzLjEwMC4xMDUuMjIxOjQwMjIvdWRwLzIzOS4yMzkuMTMuNjU6NTIzOQ=='
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC44OjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovLzYyLjc2LjI2LjgxOjgwODEvY2FuZHkvY2FuZHkwNy9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='UExBWUJPWSBSRUQ='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvYXhBUEpxWldnRC82Njk1RDA3MDgvMTgwMy50cw=='
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvYXhBUEpxWldnRC82Njk1RDA3MDgvMTY1My50cw=='
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvYXhBUEpxWldnRC82Njk1RDA3MDgvMjAwNy50cw=='
config_channel(name, url)
name='TkM='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvQ0xJRU5UWDQ4NC8zMjIyMDY1NDg3LzE5OTgudHM='
config_channel(name, url)
name='WFhYIDE='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvQ0xJRU5UWDQ4NC8zMjIyMDY1NDg3LzE5OTkudHM='
config_channel(name, url)
name='WFhYIDI='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvQ0xJRU5UWDQ4NC8zMjIyMDY1NDg3LzIwMDQudHM='
config_channel(name, url)
name='WFhYIDM='
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvQ0xJRU5UWDQ4NC8zMjIyMDY1NDg3LzIwMDEudHM='
config_channel(name, url)
name='Vk9EIDE='
url = 'aHR0cDovLzE3OC4zMy4yMjYuMzY6ODAwMC9saXZlL29sc2kvb2xzaS83OTQudHM='
config_channel(name, url)
name='Vk9EIDI='
url = 'aHR0cDovLzE3OC4zMy4yMjYuMzY6ODAwMC9saXZlL29sc2kvb2xzaS83OTMudHM='
config_channel(name, url)
name='Vk9EIDM='
url = 'aHR0cDovLzE3OC4zMy4yMjYuMzY6ODAwMC9saXZlL29sc2kvb2xzaS83OTIudHM='
config_channel(name, url)
name='Vk9EIDQ='
url = 'aHR0cDovLzE3OC4zMy4yMjYuMzY6ODAwMC9saXZlL29sc2kvb2xzaS83OTEudHM='
config_channel(name, url)
name='Vk9EIDU='
url = 'aHR0cDovLzE3OC4zMy4yMjYuMzY6ODAwMC9saXZlL29sc2kvb2xzaS83ODUudHM='
config_channel(name, url)


#############################################################################
xbmcplugin.endOfDirectory(addon_handle)