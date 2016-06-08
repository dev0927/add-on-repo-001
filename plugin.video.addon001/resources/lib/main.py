
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
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUvODAvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='SERQIDI='
url = 'aHR0cDovLzE4OC4xNjUuMjIwLjExNjo4MDgxL2xpdmUyLzUwL3BsYXlsaXN0Lm0zdTg='
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
name='QlVOR0EgQlVOR0E='
url = 'aHR0cDovLzYyLjIxMC4yNDguOTY6MTEwMDAvbGl2ZS90ZXN0L3Rlc3QvNjI1NS50cw=='
config_channel(name, url)
name='UkVETElHSFQgSEQ='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTI2OS50cw=='
config_channel(name, url)
name='UkVETElHSFQgSEQgMg=='
url = 'aHR0cDovL21haW5zdHJlYW0uZHluZG5zLnR2OjgwMDAvbGl2ZS9UVE53Y2dKYzdZL1VCTHVzWDIwaUEvOTM2LnRz'
config_channel(name, url)
name='SFVTVExFUiBUVg=='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTI2My50cw=='
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzBFOUIwMEVDRDMyNkNDQUM6QHQua3Jhc2xhbi5ydS9odXN0bGVyaGQ='
config_channel(name, url)
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTI2NS50cw=='
config_channel(name, url)
name='U1VQRVJPTkUgSEQ='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTI3My50cw=='
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
name='RVJPWA=='
url = 'aHR0cDovLzE3OC4yMDkuNzYuMTAwOjEyMzQvdWRwLzIzOS4wLjAuMjM5OjEyMzQ='
config_channel(name, url)
name='RVJPWFhY'
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTI2MC50cw=='
config_channel(name, url)
name='UElOS08gVFY='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTI2Ni50cw=='
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
url = 'aHR0cDovLzYyLjIxMC4yNDguOTY6MTEwMDAvbGl2ZS90ZXN0L3Rlc3QvNjQzMC50cw=='
config_channel(name, url)
name='RGVzaXJl'
url = 'aHR0cDovLzYyLjIxMC4yNDguOTY6MTEwMDAvbGl2ZS90ZXN0L3Rlc3QvNjI1Ny50cw=='
config_channel(name, url)
name='TWVpZGVuIHZvbiBIb2xsYW5kIEhhcmQ='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMjU1Ny50cw=='
config_channel(name, url)
name='UExBWUJPWSBSRUQ='
url = 'aHR0cDovL3B0YnJ2aXJ0dWFsLm5vLWlwLm5ldDo4MDAwL2xpdmUvYnJ1bm9zb2ZpYW1hZ2FsaGFlekBnbWFpbC5jb20vejBMeUVCME12VC8xMDMudHM='
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMjU3NS50cw=='
config_channel(name, url)
name='TkM='
url = 'aHR0cDovLzYyLjIxMC4yNDguOTY6MTEwMDAvbGl2ZS90ZXN0L3Rlc3QvNjYxNS50cw=='
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
name='SE9UIENMVUIgMQ=='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTczMS50cw=='
config_channel(name, url)
name='SE9UIENMVUIgMg=='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTczMi50cw=='
config_channel(name, url)
name='SE9UIENMVUIgMw=='
url = 'aHR0cDovL3NlcnYwMS5pcHR2cGxhbmV0LmV1OjExMTE4L2xpdmUvc293cmQvYXdvcmQvMTczMy50cw=='
config_channel(name, url)

##############################################################################
xbmcplugin.endOfDirectory(addon_handle)