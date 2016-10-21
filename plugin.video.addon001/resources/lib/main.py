
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
name='UkVETElHSFQgSEQ='
url = 'aHR0cDovLzQ2LjguMzguNTo4MDAwL3BsYXkvYTAxeA=='
config_channel(name, url)
name='SFVTVExFUiBIRCAoS1JBUyk='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9odXN0bGVyaGQ='
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
name='WFhYXzE='
url = 'aHR0cDovLzE4NS41OS4yMjAuMTM0L3gxL21wZWd0cw=='
config_channel(name, url)
name='WFhYXzI='
url = 'aHR0cDovLzE4NS41OS4yMjAuMTM0L3gyL21wZWd0cw=='
config_channel(name, url)
name='WFhYXzM='
url = 'aHR0cDovLzE4NS41OS4yMjAuMTM0L3gzL21wZWd0cw=='
config_channel(name, url)
name='WFhYXzQ='
url = 'aHR0cDovLzE4NS41OS4yMjAuMTM0L3g0L21wZWd0cw=='
config_channel(name, url)
name='WFhYXzU='
url = 'aHR0cDovLzE4NS41OS4yMjAuMTM0L3g1L21wZWd0cw=='
config_channel(name, url)
name='WFhYIFZPRA=='
url = 'aHR0cDovL2lwdHZuYXRpb24uY29tL3Bvcm4vdmlkZW8ubXA0'
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL2Nkbi0wMS5ib251cy10di5ydS9idHYvY2FuZHkvdHlwZS91c2VyL2Rldm5hbWUvTEctU21hcnRUVi9kZXZpZC9MRy0xNDY5ODE2MDU0L2VvbC8yMDIwMDEwMVQwMDAwL2hhc2gvZTgyMmYxNzdjYjQ3ODVjOTNmN2IwYTUwYTM1MzQ0MzI0NzhmNTEyYi90cmFja18yXzEwMDAvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='UExBWUJPWSBSRUQ='
url = 'aHR0cDovLzg0Ljc1Ljg3LjE2Mjo4MDAxLzE6MDoxOjUyNzo2Nzo1MzpDRTQwMDAwOjA6MDowOg=='
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovLzg0Ljc1Ljg3LjE2Mjo4MDAxLzE6MDoxOkQ1OjY2OjUzOkNFNDAwMDA6MDowOjA6'
config_channel(name, url)
name='SHVzdGxlclRW'
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NTAvMDQubTN1OA=='
config_channel(name, url)
name='RG9yY2Vs'
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjU5MDgvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgMQ=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY1OTcvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgMg=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY1OTgvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgMw=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NDkvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgNA=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NjQvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgNQ=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NjUvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgNg=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NjYvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgNw=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NjcvMDQubTN1OA=='
config_channel(name, url)
name='UGluayBFcm90aWMgOA=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NjgvMDQubTN1OA=='
config_channel(name, url)
name='QnJhenplcnNUVg=='
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NjkvMDQubTN1OA=='
config_channel(name, url)
name='UHJpdmF0ZVRW'
url = 'aHR0cDovLzkzLjg3Ljg1LjcxL1BMVFYvODg4ODg4ODgvMjI0LzMyMjEyMjY3NzAvMDQubTN1OA=='
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
name='VklLSQ=='
url = 'aHR0cDovL2VkZ2UxLmV2ZXJ5b24udHYvZXR2MXNiL3BoZDEwNzY1L3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='QnV0R08='
url = 'aHR0cDovL2VkZ2UyLmV2ZXJ5b24udHYvZXR2MnNiL3BoZDEwNzcyL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)


#############################################################################
xbmcplugin.endOfDirectory(addon_handle)