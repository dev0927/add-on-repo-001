
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
name='UGFzc2llWFhY'
url = 'cnRtcDovLzE3OC4zMy4xMjYuMjEzL2xldmVkLyBwbGF5UGF0aD1wYXNzaWVsaXZlc3RyZWFtIHN3ZlVybD1odHRwczovL3N0YXRpYy5yYW1wYW50LnR2L3N3Zi9wbGF5ZXIuc3dm'
config_channel(name, url)
name='T0xBTEE='
url = 'aHR0cDovLzRCQTlFQkRCMDdDMDU4ODM6QDUuMTU5Ljk2LjE3MDo4MDAwL29sYWxh'
config_channel(name, url)
name='T0xBTEEgMg=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9vbGFsYQ=='
config_channel(name, url)
name='T0xBTEEgMw=='
url = 'aHR0cDovLzE3OC40Ni4xNTQuMTA2OjgwMDAvcGxheS9hMDI1'
config_channel(name, url)
name='QlJBWlpFUlMgRVU='
url = 'aHR0cDovLzRCQTlFQkRCMDdDMDU4ODM6QDUuMTU5Ljk2LjE3MDo4MDAwL2JyYXp6ZXJz'
config_channel(name, url)
name='QlJBWlpFUlMgRVUgMg=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9icmF6emVycz9rcmFzdmlldy5ydQ=='
config_channel(name, url)
name='QlJBWlpFUlMgRVUgMw=='
url = 'aHR0cDovLzg3LjI0NC4xOTQuODM6ODAwMC9wbGF5L2EwMGo='
config_channel(name, url)
name='UExBWUJPWSAoRURFTSk='
url = 'aHR0cDovL3NmdHI4OWVuLmVkZW0udHYvaXB0di80RUI1U1dXRTRLOTVFUS81MjcvaW5kZXgubTN1OA=='
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVCAoRURFTSk='
url = 'aHR0cDovL3NmdHI4OWVuLmVkZW0udHYvaXB0di80RUI1U1dXRTRLOTVFUS8xNDcvaW5kZXgubTN1OA=='
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVCAyIChLUkFTKQ=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9ybg=='
config_channel(name, url)
name='UkVETElHSFQgSEQ='
url = 'aHR0cDovL3RoZXJldmVuYW50LmRkbnMubmV0OjM4ODAvbGl2ZS9lZG8xL04ycVhBU1lQNHYvMjMyLnRz'
config_channel(name, url)
name='UkVETElHSFQgSEQgMg=='
url = 'aHR0cDovL2RzLWlwdHYuZHluZG5zLm9yZzo4MDAwL2xpdmUvY29zaW1vL2Nvc2ltby8yNjI5Lm0zdTg='
config_channel(name, url)
name='SFVTVExFUiBUVg=='
url = 'aHR0cDovLzUuMTM1LjEzOS4xNDU6ODAvSHVzdGxlclRWL21vbm8ubTN1OA=='
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9odXN0bGVyaGQ='
config_channel(name, url)
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovLzE5NS4yMjguMTEuODk6NDA4MC91ZHAvMjI1LjI1NS4yNTUuNzU6MTAwMDA='
config_channel(name, url)
name='UEVOVEhPVVNFIEhEIDI='
url = 'aHR0cDovL2Vub2V6aXNhbi5ob21lLmR5bmRucy5vcmc6ODAwMC9saXZlL2FuZHJvaWQvYW5kcm9pZC81MTM1LnRz'
config_channel(name, url)
name='U1VQRVJPTkUgSEQ='
url = 'aHR0cDovL3RoZXJldmVuYW50LmRkbnMubmV0OjM4ODAvbGl2ZS9lZG8xL04ycVhBU1lQNHYvMjM2LnRz'
config_channel(name, url)
name='UFJJVkFURQ=='
url = 'aHR0cDovLzUuMTM1LjEzOS4xNDU6ODAvUHJpdmF0ZV9UVi9tb25vLm0zdTg='
config_channel(name, url)
name='RE9SQ0VM'
url = 'aHR0cDovL2Vub2V6aXNhbi5ob21lLmR5bmRucy5vcmc6ODAwMC9saXZlL2FuZHJvaWQvYW5kcm9pZC80ODE2LnRz'
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovL2Vub2V6aXNhbi5ob21lLmR5bmRucy5vcmc6ODAwMC9saXZlL2FuZHJvaWQvYW5kcm9pZC81MTQ3LnRz'
config_channel(name, url)
name='RVJPWFhY'
url = 'aHR0cDovLzUuMTM1LjEzOS4xNDU6ODAvRXJveHh4X0hEL21vbm8ubTN1OA=='
config_channel(name, url)
name='TEVP'
url = 'aHR0cDovLzUuMTM1LjEzOS4xNDU6ODAvTGVvX1RWL21vbm8ubTN1OA=='
config_channel(name, url)
name='TklHSFQgQ0xVQg=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9uY2x1Yg=='
config_channel(name, url)
name='TmNreXdlaG5l'
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9pc2t1cw=='
config_channel(name, url)
name='RlJFQ0hMT1ZFUg=='
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC43OjEyMzQ='
config_channel(name, url)
name='WFhM'
url = 'aHR0cDovLzk0LjI1My41Mi4xOTo3Nzg4L3VkcC8yMzQuNS4yLjI0NjoxMjM0'
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC44OjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovLzM3LjIzNS4xNDcuMjUwOjgxL3VkcC8yMjUuNTAuNzAuMToxMjM0'
config_channel(name, url)
name='UElOSyBP'
url = 'aHR0cDovL3ZoLmdvbGR0di5hbDo4MDAwL2xpdmUvdG9tL3RvbS8xMDkxLnRz'
config_channel(name, url)
name='U0VYVFJFTUU='
url = 'aHR0cDovL2Vub2V6aXNhbi5ob21lLmR5bmRucy5vcmc6ODAwMC9saXZlL2FuZHJvaWQvYW5kcm9pZC81MTI2LnRz'
config_channel(name, url)
name='Q2luZGVyZWxsYSBYWFg='
url = 'aHR0cDovL2RzLWlwdHYuZHluZG5zLm9yZzo4MDAwL21vdmllL2Nvc2ltby9jb3NpbW8vMjc2NS5ta3Y='
config_channel(name, url)
name='Q2FtU29kYSBLaXRjaGVu'
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1raXRjaGVuLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBNYXN0ZXIgQmVkcm9vbSBB'
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1tYXN0ZXItYmVkcm9vbS1hLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBFeGVyY2lzZSBSb29t'
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1leGVyY2lzZS5zdHJlYW0vcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='Q2FtU29kYSBUaGVhdGVyIFJvb20='
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS10aGVhdGVyLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBUaGF0IDcwcyBSb29t'
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS10aGF0NzBzcm9vbS5zdHJlYW0vcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='Q2FtU29kYSBUaGF0IDcwcyBTaG93ZXI='
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS03MHMtc2hvd2VyLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBHaXJscyBSb29t'
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1naXJscy1yb29tLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBHaXJscyBTaG93ZXI='
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1naXJscy1zaG93ZXIuc3RyZWFtL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='Q2FtU29kYSBTaG93ZXI='
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1zaG93ZXIuc3RyZWFtL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='Q2FtU29kYSBQb29s'
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1wb29sLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBTbHVtYmVyIFBhcnR5'
url = 'aHR0cDovLzE5OS44OC41OS4yNDU6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1zbHVtYmVyLXBhcnR5LnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBQYXRpbw=='
url = 'aHR0cDovLzE5OS44OC41OS4yNDU6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1wYXRpby5zdHJlYW0vcGxheWxpc3QubTN1OA=='
config_channel(name, url)


##############################################################################
xbmcplugin.endOfDirectory(addon_handle)