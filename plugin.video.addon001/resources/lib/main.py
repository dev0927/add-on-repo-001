
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
url = 'aHR0cDovL3VzYXNlcnZlci5taWFtaXR2Y2hhbm5lbC5jb20vbWlhbWl0di9zbWlsOm1pYW1pdHYvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='U1VQRVJPTkUgSEQ='
url = 'aHR0cDovLzMxLjIyMy4yMzguMTA6ODAwMS8xOjA6MTo0MDk6MjoxOkUwODMxQjM6MDowOjA6'
config_channel(name, url)
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovLzUuMzIuMTMyLjIxOTo0MDgwL3VkcC8yMzAuMS4xLjE2OjEwMDA='
config_channel(name, url)
name='UEVOVEhPVVNFIEhEIDI='
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
name='UFJJVkFURSAoRVJPKQ=='
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL24yNDA5IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcvZXVyb3RpY190dl9vbmxpbmUv'
config_channel(name, url)
name='RE9SQ0VMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24yMDI0IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcvZXVyb3RpY190dl9vbmxpbmUv'
config_channel(name, url)
name='WFhMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL244MTUzIHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcvZXVyb3RpY190dl9vbmxpbmUv'
config_channel(name, url)
name='T2xhbGEgKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24yNDggcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='TnVhcnQgKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24xODcgcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='RXJvdGljIChFUk8p'
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL2NfOTE2IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcvZXVyb3RpY190dl9vbmxpbmUv'
config_channel(name, url)
name='WFhY'
url = 'aHR0cDovLzc4LjQ2LjY0LjEzOjE5MzUvdHYzL215U3RyZWFtL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='WFhYIFZPRA=='
url = 'aHR0cDovL2lwdHZuYXRpb24uY29tL3Bvcm4vdmlkZW8ubXA0'
config_channel(name, url)
name='RVJPWA=='
url = 'aHR0cDovLzE4NS40NC43My4xMi9FUk9YL2luZGV4Lm0zdTg='
config_channel(name, url)
name='RVJPWFhY'
url = 'aHR0cDovLzE4NS40NC43My4xMi9FUk9YWFhfSEQvaW5kZXgubTN1OA=='
config_channel(name, url)
name='UkVETElHSFQgSEQ='
url = 'aHR0cDovLzQ2LjguMzguNTo4MDAwL3BsYXkvYTAxeA=='
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4xODAuMjE3OjgxL3VkcC8yMjUuNTAuNzAuODoxMjM0'
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL2Nkbi0wNC5ib251cy10di5ydS9idHYvY2FuZHkvdHlwZS91c2VyL2Rldm5hbWUvTEctU21hcnRUVi9kZXZpZC9MRy0xNDY5ODE2MDU0L2VvbC8yMDIwMDEwMVQwMDAwL2hhc2gvZTgyMmYxNzdjYjQ3ODVjOTNmN2IwYTUwYTM1MzQ0MzI0NzhmNTEyYi90cmFja18yXzEwMDAvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovLzM3LjIzNS4xODAuMjE3OjgxL3VkcC8yMjUuNTAuNzAuMToxMjM0'
config_channel(name, url)
name='UExBWUJPWSBSRUQ='
url = 'aHR0cDovL3N0cmVhbS56ZXRhdHYuY2YvcHcvcGxheWJveV8xM3QycWYzL2NodW5rbGlzdC5tM3U4'
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovL3N0cmVhbS56ZXRhdHYuY2YvcHcvdmVudXNfYjlkNXA3MS9jaHVua2xpc3QubTN1OA=='
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovL2dsb2JpcHR2LmNvbTo4MDAwL2xpdmUvc2FpYi9mYXJlcy8yMDA3LnRz'
config_channel(name, url)
name='SkFTTUlO'
url = 'cnRtcDovLzEwOS43MS4xNjIuMTEyL2xpdmUvaGQuamFzbWluY2hhbm5lbC5zdHJlYW0vaGQuamFzbWluY2hhbm5lbC5zdHJlYW0='
config_channel(name, url)
name='VklTVC1Y'
url = 'aHR0cDovL3N0cmVhbS52aXNpdC14LnR2L3Z4dHYvbGl2ZV83MjBwL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='Rk9YIEI='
url = 'aHR0cDovL3B1Ymxpc2gudGhld2Vic3RyZWFtLmNvOjE5MzUvbGV2ZWQvX2RlZmluc3RfL2ZveHh4YmFiZXMvcGxheWxpc3QubTN1OA=='
config_channel(name, url)


#############################################################################
xbmcplugin.endOfDirectory(addon_handle)