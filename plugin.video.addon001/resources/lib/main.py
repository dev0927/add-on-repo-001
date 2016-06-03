
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
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUvNzcvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='SERQIDI='
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUyLzQ3L3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='T0xBTEEgKEtSQVMp'
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9vbGFsYQ=='
config_channel(name, url)
name='QlJBWlpFUlMgRVUgKEtSQVMp'
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9icmF6emVycw=='
config_channel(name, url)
name='QlJBWlpFUlMgRVUgSEM='
url = 'aHR0cDovLzE3OC40Ni4xNTQuMTA2OjgwMDAvcGxheS9hMDBo'
config_channel(name, url)
name='UExBWUJPWSAoS1JBUyk='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9wbGF5Ym95'
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVCAoS1JBUyk='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9ybg=='
config_channel(name, url)
name='UkVETElHSFQgSEQ='
url = 'aHR0cDovL2dhbWVzZXJ2ZXIxLnN0cmVhbWlwdHYub25saW5lOjE5MDAxL2xpdmUvaFZ3Z0ZqN2NLVS9ZYXgyeVhWeklnLzI2MzgudHM='
config_channel(name, url)
name='UkVETElHSFQgSEQgMg=='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9hbGVzYW5kcm8vYWxlc2FuZHJvLzExMTYudHM='
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9odXN0bGVyaGQ='
config_channel(name, url)
name='UFJJVkFURSAoRVJPKQ=='
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL24xMDI0IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='RE9SQ0VMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24xODEwIHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='RG9yY2VsIENsdWI='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTA2LnRz'
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
name='WFhMKEVSTyk='
url = 'aHR0cDovLzk0LjI1My41Mi4xOTo3Nzg4L3VkcC8yMzQuNS4yLjI0NjoxMjM0'
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC44OjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL2Nkbi0wMS5ib251cy10di5ydS9UVkI3L2NhbmR5L3RyYWNrXzBfMzAwMC9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='RFVTSw=='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTA3LnRz'
config_channel(name, url)
name='TWVpZGVuIHZvbiBIb2xsYW5kIEhhcmQ='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTEyLnRz'
config_channel(name, url)
name='RUE='
url = 'aHR0cDovL2Z0dm5leHQuc3RtdGVhbS5vcmc6ODAwMC9saXZlL2RlbGlhL2RlbGlhLzE0OS50cw=='
config_channel(name, url)
name='TkM='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTEzLnRz'
config_channel(name, url)
name='U0VYVFJFTUU='
url = 'aHR0cDovL2Z0dm5leHQuc3RtdGVhbS5vcmc6ODAwMC9saXZlL2RlbGlhL2RlbGlhLzI0MDYudHM='
config_channel(name, url)
name='UElOSyBFUk9USUM='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9hbGVzYW5kcm8vYWxlc2FuZHJvLzExMTUudHM='
config_channel(name, url)
name='UElOSyBFUk9USUMgMg=='
url = 'aHR0cDovL2NwLmRtYnNoYXJlLm5ldDo4MDAwL2xpdmUvbWljaGFlbDEvbWljaGFlbDEvMjkxOC50cw=='
config_channel(name, url)
name='UElOSyBFUk9USUMgMw=='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9hbGVzYW5kcm8vYWxlc2FuZHJvLzExMTcudHM='
config_channel(name, url)
name='UElOSyBFUk9USUMgNA=='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9hbGVzYW5kcm8vYWxlc2FuZHJvLzExMTgudHM='
config_channel(name, url)
name='WFhYIDE='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTEzLnRz'
config_channel(name, url)
name='WFhYIDI='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTA1LnRz'
config_channel(name, url)
name='WFhYIDM='
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTA5LnRz'
config_channel(name, url)
name='WFhYIDQ='
url = 'aHR0cDovL2d0YXRlbXZvZC5jb206NDMxMDAvbW92aWUvZ3VnbGllbG1vL2d1Z2xpZWxtby8xNDE4OC5ta3Y='
config_channel(name, url)
name='WFhYIDU='
url = 'aHR0cDovL2d0YXRlbXZvZC5jb206NDMxMDAvbW92aWUvZ3VnbGllbG1vL2d1Z2xpZWxtby8xNDE4Ny5ta3Y='
config_channel(name, url)
name='WFhYIDY='
url = 'aHR0cDovL2d0YXRlbXZvZC5jb206NDMxMDAvbW92aWUvZ3VnbGllbG1vL2d1Z2xpZWxtby8xNDE5NC5ta3Y='
config_channel(name, url)
name='WFhYIDc='
url = 'aHR0cDovL2d0YXRlbXZvZC5jb206NDMxMDAvbW92aWUvZ3VnbGllbG1vL2d1Z2xpZWxtby8xNDIxOC5ta3Y='
config_channel(name, url)
name='WFhYIDg='
url = 'aHR0cDovL2d0YXRlbXZvZC5jb206NDMxMDAvbW92aWUvZ3VnbGllbG1vL2d1Z2xpZWxtby8xNDIxNS5ta3Y='
config_channel(name, url)
name='WFhYIDk='
url = 'aHR0cDovL2d0YXRlbXZvZC5jb206NDMxMDAvbW92aWUvZ3VnbGllbG1vL2d1Z2xpZWxtby8xNDIxNC5ta3Y='
config_channel(name, url)
name='WFhYIDEw'
url = 'aHR0cDovL09SQklULUlQVFYuQ09NOjI1MDAvbGl2ZS8zMDMwLzMwMzAvMjUyLnRz'
config_channel(name, url)
name='WFhYIDEx'
url = 'aHR0cDovL09SQklULUlQVFYuQ09NOjI1MDAvbGl2ZS8zMDMwLzMwMzAvMjkwLnRz'
config_channel(name, url)
name='WFhYIDEy'
url = 'aHR0cDovL09SQklULUlQVFYuQ09NOjI1MDAvbGl2ZS8zMDMwLzMwMzAvMTExMC50cw=='
config_channel(name, url)
name='WFhYIDEz'
url = 'aHR0cDovL09SQklULUlQVFYuQ09NOjI1MDAvbGl2ZS9vbWFuL29tYW4vNTQudHM='
config_channel(name, url)
name='UlAgMDAx'
url = 'aHR0cDovLzE5NS4xNTQuMTgzLjQ4OjgwMDAvbGl2ZS9yb2JlcnRvMS9yb2JlcnRvMS8xMTM2LnRz'
config_channel(name, url)
name='NEsgMDAx'
url = 'aHR0cDovL3d3dy5lbGJveHR2LmNvbToxOTg1L2xpdmUvYWxsL3Rlc3RzLzIyODgudHM='
config_channel(name, url)
name='NEsgMDAy'
url = 'aHR0cDovL3d3dy5lbGJveHR2LmNvbToxOTg1L2xpdmUvYWxsL3Rlc3RzLzI0OTEudHM='
config_channel(name, url)



##############################################################################
xbmcplugin.endOfDirectory(addon_handle)