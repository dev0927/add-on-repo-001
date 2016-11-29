
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
name='UElOS08gVFY='
url = 'aHR0cDovLzQ2LjguMzguNTo4MDAwL3BsYXkvYTAzaA=='
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
url = 'cnRtcDovLzUuMTk2LjE4OS4zOS9saXZlL24yNDA5IHBhZ2VVcmw9aHR0cDovL2Vyby10di5vcmcv'
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
name='Q1hD'
url = 'aHR0cDovL2tkc2Fqa2xkc2FkanNhYjc3Njc2ZHNhOTlzYWdoZHNoaGRkcy5zaXRlbm93Lm1lL2xpdmUvaG90X2FzbjNjbnYvcGxheWxpc3QubTN1OHxVc2VyLUFnZW50PU1vemlsbGElMmY1LjAmcmVmZXJlcj1odHRwOi8vd3d3LnBvbmxhdHYuY29t'
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
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovL2tkc2Fqa2xkc2FkanNhYjc3Njc2ZHNhOTlzYWdoZHNoaGRkcy5zaXRlbm93Lm1lL2xpdmUvcGVudGhvdXNlX2JpZDB1MXEvcGxheWxpc3QubTN1OHxVc2VyLUFnZW50PU1vemlsbGElMmY1LjAmcmVmZXJlcj1odHRwOi8vd3d3LnBvbmxhdHYuY29t'
config_channel(name, url)
name='WFhY'
url = 'aHR0cDovLzc4LjQ2LjY0LjEzOjE5MzUvdHYzL215U3RyZWFtL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='TElWRQ=='
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUvMDIxL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='TElWRSAy'
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUyLzAyMS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='TElWRSAz'
url = 'aHR0cDovL2xpdmUuc29mdGlwdHYuY29tOjk5MDAvbGl2ZS81MjUvNTI1LzEyMjczLnRz'
config_channel(name, url)
name='WFhYIFZPRA=='
url = 'aHR0cDovL2lwdHZuYXRpb24uY29tL3Bvcm4vdmlkZW8ubXA0'
config_channel(name, url)
name='RVJPWFhY'
url = 'aHR0cDovL2hvbWV0di5pcHR2c2VydmVyLm9ubGluZTo4MDAwL2xpdmUvZ29yY3VtNzQ1OC84NTQ3MjEyMy80NzQudHM='
config_channel(name, url)
name='RVhUQVNZ'
url = 'aHR0cDovL2hvbWV0di5pcHR2c2VydmVyLm9ubGluZTo4MDAwL2xpdmUvZ29yY3VtNzQ1OC84NTQ3MjEyMy80ODMudHM='
config_channel(name, url)
name='Uks='
url = 'aHR0cDovL2hvbWV0di5pcHR2c2VydmVyLm9ubGluZTo4MDAwL2xpdmUvZ29yY3VtNzQ1OC84NTQ3MjEyMy80ODEudHM='
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovL2lwdHYubW9ua2V5Y2xpbmUuY29tOjI1NDYxL2xpdmUvamFzbmUvamFzbmUvMjYzNy50cw=='
config_channel(name, url)
name='RlJFTkNITE9WRVI='
url = 'aHR0cDovLzM3LjIzNS4xNjYuODE6ODEvdWRwLzIyNS41MC43MC43OjEyMzQ='
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4xNjYuODE6ODEvdWRwLzIyNS41MC43MC44OjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL2Nkbi0wMS5ib251cy10di5ydS9idHYvY2FuZHkvdHlwZS91c2VyL2Rldm5hbWUvTEctU21hcnRUVi9kZXZpZC9MRy0xNDY5ODE2MDU0L2VvbC8yMDIwMDEwMVQwMDAwL2hhc2gvZTgyMmYxNzdjYjQ3ODVjOTNmN2IwYTUwYTM1MzQ0MzI0NzhmNTEyYi90cmFja18yXzEwMDAvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='RFVTSw=='
url = 'aHR0cDovL2hvbWV0di5pcHR2c2VydmVyLm9ubGluZTo4MDAwL2xpdmUvZ29yY3VtNzQ1OC84NTQ3MjEyMy80ODIudHM='
config_channel(name, url)
name='TWVpZGVuIHZvbiBIb2xsYW5kIEhhcmQ='
url = 'aHR0cDovL2xpdmUuc29mdGlwdHYuY29tOjk5MDAvbGl2ZS81MjUvNTI1LzEyNTE1LnRz'
config_channel(name, url)
name='VklQIDE='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi82MS50cw=='
config_channel(name, url)
name='VklQIDI='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi82Mi50cw=='
config_channel(name, url)
name='VklQIDM='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8xOTQ5LnRz'
config_channel(name, url)
name='VklQIDQ='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8xOTUxLnRz'
config_channel(name, url)
name='VklQIDU='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8xOTUyLnRz'
config_channel(name, url)
name='VklQIDY='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yNjIudHM='
config_channel(name, url)
name='VklQIDc='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yNjMudHM='
config_channel(name, url)
name='VklQIDg='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yNjYudHM='
config_channel(name, url)
name='VklQIDk='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yNjcudHM='
config_channel(name, url)
name='VklQIDEw'
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yNjgudHM='
config_channel(name, url)
name='QURVTFQgNzg='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi83OC50cw=='
config_channel(name, url)
name='QURVTFQgMjY0'
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yNjQudHM='
config_channel(name, url)
name='QURVTFQgMjY1'
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yNjUudHM='
config_channel(name, url)
name='QURVTFQgMTk1MA=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8xOTUwLnRz'
config_channel(name, url)
name='QURVTFQgMjMzNA=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzM0LnRz'
config_channel(name, url)
name='QURVTFQgMjMzNQ=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzM1LnRz'
config_channel(name, url)
name='QURVTFQgMjMzNg=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzM2LnRz'
config_channel(name, url)
name='QURVTFQgMjMzNw=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzM3LnRz'
config_channel(name, url)
name='QURVTFQgMjMzOA=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzM4LnRz'
config_channel(name, url)
name='QURVTFQgMjMzOQ=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzM5LnRz'
config_channel(name, url)
name='QURVTFQgMjM0MA=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzQwLnRz'
config_channel(name, url)
name='QURVTFQgMjM0MQ=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzQxLnRz'
config_channel(name, url)
name='QURVTFQgMjM0Mg=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzQyLnRz'
config_channel(name, url)
name='QURVTFQgMjM0Mw=='
url = 'aHR0cDovL2J1cjg3OS5jb206ODAwMC9saXZlL3RvbXk2NTY1Lzc4MjkwZi8yMzQzLnRz'
config_channel(name, url)
name='WCA5'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzUzLnRz'
config_channel(name, url)
name='WCA4'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzUyLnRz'
config_channel(name, url)
name='WCA3'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzUxLnRz'
config_channel(name, url)
name='WCA2'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzUwLnRz'
config_channel(name, url)
name='WCA1'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzQ5LnRz'
config_channel(name, url)
name='WCA0'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzQ4LnRz'
config_channel(name, url)
name='WCAz'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzQ3LnRz'
config_channel(name, url)
name='WCAy'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzQ2LnRz'
config_channel(name, url)
name='WCAx'
url = 'aHR0cDovLzM3LjE4Ny4xMjguMTY5OjgwMDAvbGl2ZS81NDVkZmtkamkvYXNrZGhma2FqNDc3ZWVqLzQ1LnRz'
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