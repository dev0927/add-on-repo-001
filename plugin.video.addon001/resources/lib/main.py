
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

#############################################################################

name='TWlhbWkgVFY='
url = 'aHR0cDovL3VzYXNlcnZlci5taWFtaXR2Y2hhbm5lbC5jb20vbWlhbWl0di9zbWlsOm1pYW1pdHYvcGxheWxpc3QubTN1OA=='
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
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL24zMTQ3IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='RE9SQ0VMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24yMDI0IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='WFhMKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL244MTUzIHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
config_channel(name, url)
name='T2xhbGEgKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24yNDggcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='TnVhcnQgKEVSTyk='
url = 'cnRtcDovLzUuMTk2LjIwMC4yMjg6MTkzOS9saXZlL24xODcgcGFnZVVybD1odHRwOi8vZXJvLXR2Lm9yZy8='
config_channel(name, url)
name='UGFzc2llWFhYIChFUk8p'
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL2NfOTE2IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcvZXVyb3RpY190dl9vbmxpbmUv'
config_channel(name, url)
name='SFVTVExFUiBUVg=='
url = 'aHR0cDovL2tkc2Fqa2xkc2FkanNhYjc3Njc2ZHNhOTlzYWdoZHNoaGRkcy5zaXRlbm93Lm1lL2xpdmUvaHVzdGxlcnR2XzljN28ybTIvcGxheWxpc3QubTN1OHxVc2VyLUFnZW50PU1vemlsbGElMmY1LjAmcmVmZXJlcj1odHRwOi8vd3d3LnBvbmxhdHYuY29t'
config_channel(name, url)
name='UEIgUkVE'
url = 'aHR0cDovL2tkc2Fqa2xkc2FkanNhYjc3Njc2ZHNhOTlzYWdoZHNoaGRkcy5zaXRlbm93Lm1lL2xpdmUvcGxheWJveV8xM3QycWYzL3BsYXlsaXN0Lm0zdTh8VXNlci1BZ2VudD1Nb3ppbGxhJTJmNS4wJnJlZmVyZXI9aHR0cDovL3d3dy5wb25sYXR2LmNvbQ=='
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovL2tkc2Fqa2xkc2FkanNhYjc3Njc2ZHNhOTlzYWdoZHNoaGRkcy5zaXRlbm93Lm1lL2xpdmUvdmVudXNfMTU3eTM3OS9wbGF5bGlzdC5tM3U4fFVzZXItQWdlbnQ9TW96aWxsYSUyZjUuMCZyZWZlcmVyPWh0dHA6Ly93d3cucG9ubGF0di5jb20='
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9saXZlL21hbi9NQU4vNTc3Mi50cw=='
config_channel(name, url)
name='QkxVRSBIVVNUTEVS'
url = 'aHR0cDovLzE3OC4xMjQuMTgzLjEwL2hscy9DSF9CTFVFSFVTVExFUi92YXJpYW50Lm0zdTg/dmVyc2lvbj0y'
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVA=='
url = 'aHR0cDovLzE3OC4xMjQuMTgzLjEwL2hscy9DSF9SVVNTS0FZQU5PQ0gvdmFyaWFudC5tM3U4P3ZlcnNpb249Mg=='
config_channel(name, url)
name='TlVBUlQ='
url = 'aHR0cDovLzE3OC4xMjQuMTgzLjE1OjgwL2hscy9DSF9OWUFSVFRWL3ZhcmlhbnQubTN1OD92ZXJzaW9uPTI='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL2Nkbi0wMS5ib251cy10di5ydS9idHYvY2FuZHkvdHlwZS91c2VyL2Rldm5hbWUvTEctU21hcnRUVi9kZXZpZC9MRy0xNDY5ODE2MDU0L2VvbC8yMDIwMDEwMVQwMDAwL2hhc2gvZTgyMmYxNzdjYjQ3ODVjOTNmN2IwYTUwYTM1MzQ0MzI0NzhmNTEyYi90cmFja18yXzEwMDAvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='UElOSyBP'
url = 'aHR0cDovL2xpdmUuc29mdGlwdHYuY29tOjk5MDAvbGl2ZS81MjUvNTI1LzEyNTI2LnRz'
config_channel(name, url)
name='UEFTU0lFWFhY'
url = 'aHR0cDovL2xpdmUuc29mdGlwdHYuY29tOjk5MDAvbGl2ZS81MjUvNTI1LzEyNTI1LnRz'
config_channel(name, url)
name='TWVpZGVuIHZvbiBIb2xsYW5kIEhhcmQ='
url = 'aHR0cDovL2xpdmUuc29mdGlwdHYuY29tOjk5MDAvbGl2ZS81MjUvNTI1LzEyNTE1LnRz'
config_channel(name, url)
name='RVJPWFhYIEhE'
url = 'aHR0cHM6Ly9jZG4xLjRuZXQudHYvbWFzdGVyXzEwMTIubTN1OA=='
config_channel(name, url)
name='RVJPWCBIRA=='
url = 'aHR0cHM6Ly9jZG4xLjRuZXQudHYvbWFzdGVyXzEwMTMubTN1OA=='
config_channel(name, url)
name='WFhYIFZPRA=='
url = 'aHR0cDovL2lwdHZuYXRpb24uY29tL3Bvcm4vdmlkZW8ubXA0'
config_channel(name, url)
name='UFJJVkFURQ=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAveDEvbXBlZ3RzLw=='
config_channel(name, url)
name='QkxBQ0tFRA=='
url = 'aHR0cDovL2xpdmUuc29mdGlwdHYuY29tOjk5MDAvbGl2ZS81MjUvNTI1LzEyMDY4LnRz'
config_channel(name, url)
name='QURVTFQgMQ=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAveDIvbXBlZ3RzLw=='
config_channel(name, url)
name='QURVTFQgMg=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAveDMvbXBlZ3RzLw=='
config_channel(name, url)
name='QURVTFQgMw=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAveDUvbXBlZ3RzLw=='
config_channel(name, url)
name='UGVudGhvdXNlIEhEIDE='
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9saXZlL21hbi9NQU4vNDE1Ni50cw=='
config_channel(name, url)
name='TnVhcnQgVFY='
url = 'aHR0cDovL2ZyYW5jZS50dnNuZy5jb206MjU0NjEvbGl2ZS90ZXN0MjAxNy90ZXN0MjAxNy81NzMudHM='
config_channel(name, url)
name='QnJhenplcnMgVFY='
url = 'aHR0cDovL2ZyYW5jZS50dnNuZy5jb206MjU0NjEvbGl2ZS90ZXN0MjAxNy90ZXN0MjAxNy81ODEudHM='
config_channel(name, url)
name='RG9yY2VsIEhE'
url = 'aHR0cDovL2ZyYW5jZS50dnNuZy5jb206MjU0NjEvbGl2ZS90ZXN0MjAxNy90ZXN0MjAxNy81NzkudHM='
config_channel(name, url)
name='UmVkbGlnaHQgSEQ='
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9saXZlL21hbi9NQU4vNDk0MS50cw=='
config_channel(name, url)
name='UnVzc2lhbiBOaWdodA=='
url = 'aHR0cDovL2ZyYW5jZS50dnNuZy5jb206MjU0NjEvbGl2ZS90ZXN0MjAxNy90ZXN0MjAxNy81MTgudHM='
config_channel(name, url)
name='Qmx1ZSBIdXN0bGVy'
url = 'aHR0cDovL2ZyYW5jZS50dnNuZy5jb206MjU0NjEvbGl2ZS90ZXN0MjAxNy90ZXN0MjAxNy81MjAudHM='
config_channel(name, url)
name='VklQIDE='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzYxLnRz'
config_channel(name, url)
name='VklQIDI='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzYyLnRz'
config_channel(name, url)
name='VklQIDM='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzE5NDkudHM='
config_channel(name, url)
name='VklQIDQ='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzE5NTEudHM='
config_channel(name, url)
name='VklQIDU='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzE5NTIudHM='
config_channel(name, url)
name='VklQIDY='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzI2Mi50cw=='
config_channel(name, url)
name='VklQIDc='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzI2My50cw=='
config_channel(name, url)
name='VklQIDg='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzI2Ni50cw=='
config_channel(name, url)
name='VklQIDk='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzI2Ny50cw=='
config_channel(name, url)
name='VklQIDEw'
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzI2OC50cw=='
config_channel(name, url)
name='QURVTFQgNzg='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzc4LnRz'
config_channel(name, url)
name='QURVTFQgMjY0'
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzI2NC50cw=='
config_channel(name, url)
name='QURVTFQgMjY1'
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzI2NS50cw=='
config_channel(name, url)
name='QURVTFQgMTk1MA=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzE5NTAudHM='
config_channel(name, url)
name='QURVTFQgMjMzNA=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzMzQudHM='
config_channel(name, url)
name='QURVTFQgMjMzNQ=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzMzUudHM='
config_channel(name, url)
name='QURVTFQgMjMzNg=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzMzYudHM='
config_channel(name, url)
name='QURVTFQgMjMzNw=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzMzcudHM='
config_channel(name, url)
name='QURVTFQgMjMzOA=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzMzgudHM='
config_channel(name, url)
name='QURVTFQgMjMzOQ=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzMzkudHM='
config_channel(name, url)
name='QURVTFQgMjM0MA=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzNDAudHM='
config_channel(name, url)
name='QURVTFQgMjM0MQ=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzNDEudHM='
config_channel(name, url)
name='QURVTFQgMjM0Mg=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzNDIudHM='
config_channel(name, url)
name='QURVTFQgMjM0Mw=='
url = 'aHR0cDovL3RlY2gzNDMuY29tOjgwMDAvbGl2ZS9PS1RBWTEvT0tUQVkxLzIzNDMudHM='
config_channel(name, url)
name='UGluayBFcm90aWMgMQ=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAvZXJvdGljMS9tcGVndHM='
config_channel(name, url)
name='UGluayBFcm90aWMgMg=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAvZXJvdGljMi9tcGVndHM='
config_channel(name, url)
name='UGluayBFcm90aWMgMw=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAvZXJvdGljMy9tcGVndHM='
config_channel(name, url)
name='UGluayBFcm90aWMgNA=='
url = 'aHR0cDovLzE4NS4xNTIuNjUuMTMxOjgwODAvZXJvdGljNC9tcGVndHM='
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