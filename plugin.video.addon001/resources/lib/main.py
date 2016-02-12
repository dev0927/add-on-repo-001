
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
name='QlJBWlpFUlMgRVU='
url = 'aHR0cDovLzRCQTlFQkRCMDdDMDU4ODM6QDUuMTU5Ljk2LjE3MDo4MDAwL2JyYXp6ZXJz'
config_channel(name, url)
name='QlJBWlpFUlM='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMTIxL3N0b2xlbi8wNTFzL3Ryb2phbi5leGU='
config_channel(name, url)
name='SFVTVExFUiBUVg=='
url = 'aHR0cDovLzkzLjg3LjY0LjI0NDo0MDgwL3VkcC8yMjcuMS41LjE6MTAwMA=='
config_channel(name, url)
name='UExBWUJPWSAoRURFTSk='
url = 'aHR0cDovL3NmdHI4OWVuLmVkZW0udHYvaXB0di80RUI1U1dXRTRLOTVFUS81MjcvaW5kZXgubTN1OA=='
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVCAoRURFTSk='
url = 'aHR0cDovL3NmdHI4OWVuLmVkZW0udHYvaXB0di80RUI1U1dXRTRLOTVFUS8xNDcvaW5kZXgubTN1OA=='
config_channel(name, url)
name='TlVBUlQ='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjYxL3N0b2xlbi8zMjVlL2NvbG9ycy5kbWc='
config_channel(name, url)
name='UkVETElHSFQgSEQ='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMTExL3N0b2xlbi8wNTJ3L3J1dGtpdC5leGU='
config_channel(name, url)
name='UEFTU0lPTiBYWFg='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjgxL3N0b2xlbi8zNzJzL3JhaW5ib3cudWRm'
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMTExL3N0b2xlbi8wNTNlL3J1dGtpdC5leGU='
config_channel(name, url)
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovLzkzLjg3LjY0LjI0NDo0MDgwL3VkcC8yMjcuMS40LjE2OjEwMDA='
config_channel(name, url)
name='U1VQRVJPTkUgSEQ='
url = 'aHR0cDovLzMxLjIyMy4yMzguMTA6ODAwMS8xOjA6MTo0MDk6MjoxOkUwODMxQjM6MDowOjA6'
config_channel(name, url)
name='VklWSUQ='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjUxL3N0b2xlbi8zMzZ2L29uZWhhbGYuY2Fi'
config_channel(name, url)
name='UFJJVkFURSBHT0xE'
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMzQxL3N0b2xlbi80ODJ4L2RlbGV0ZS5wcm9ncmFtbTMyX3N0YXJ0Lm5zaXM='
config_channel(name, url)
name='RE9SQ0VM'
url = 'aHR0cDovLzc3Ljc2LjE0MC4yNTE6MjI2MzcvdWRwLzIzMS4xLjEuMjU6MTIzNA=='
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjAxL3N0b2xlbi8yNTJ4L3hlbml4b3MuN3o='
config_channel(name, url)
name='UkVBTElUWSBLSU5H'
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMTYxL3N0b2xlbi8xNTdkL3BhcmFzaXRlLmluc3RhbGw='
config_channel(name, url)
name='RVJPWFhY'
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMzcxL3N0b2xlbi8wMjUvZHVxdQ=='
config_channel(name, url)
name='RVJPWA=='
url = 'aHR0cDovLzIxNy4xNDcuNDAuMTE4OjgwODAvdWRwLzIzMy45Ny4yMC4xODI6MTIzNA=='
config_channel(name, url)
name='RVhPVElDQQ=='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjgxL3N0b2xlbi8zNjdnL3JhaW5ib3cudWRm'
config_channel(name, url)
name='U0FUSVNGQUNUSU9O'
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjgxL3N0b2xlbi8zNjVhL3JhaW5ib3cudWRm'
config_channel(name, url)
name='UElOS08gVFY='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjgxL3N0b2xlbi8zNzNiL3JhaW5ib3cudWRm'
config_channel(name, url)
name='U0VYVE8gNiBTRU5TTw=='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMjgxL3N0b2xlbi8zNzFlL3JhaW5ib3cudWRm'
config_channel(name, url)
name='T0xBTEE='
url = 'aHR0cDovLzkxLjIwNC4yMTQuMTA2OjIzMzAxL3N0b2xlbi80NDFsL3ZpcnV0LmNobQ=='
config_channel(name, url)
name='TklHSFQgQ0xVQg=='
url = 'aHR0cDovLzQ2LjE4MS4yMzcuNzU6MTIzNC91ZHAvMjM5LjI1NS40Mi4yMTc6MTIzNA=='
config_channel(name, url)
name='RlJFQ0hMT1ZFUg=='
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC43OjEyMzQ='
config_channel(name, url)
name='WFhM'
url = 'aHR0cDovLzg3LjI0Ni4wLjEzNDo1OTM0OS90dl9YWEw='
config_channel(name, url)
name='RlJFRS1Y'
url = 'aHR0cDovLzM3LjIzNS4yMTYuMjU1OjQwMDAvdWRwLzIyNS41MC43MC44OjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovLzYyLjc2LjI2LjgxOjgwODEvY2FuZHkvY2FuZHkvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='UElOSyBFUk9USUM='
url = 'aHR0cDovLzQ2LjIzNC4xMDAuNDE6ODA4MC9lcm90aWMxL2luZGV4Lm0zdTg='
config_channel(name, url)
name='UElOSyBFUk9USUMgMg=='
url = 'aHR0cDovLzQ2LjIzNC4xMDAuNDE6ODA4MC9lcm90aWMyL2luZGV4Lm0zdTg='
config_channel(name, url)
name='UElOSyBFUk9USUMgMw=='
url = 'aHR0cDovLzQ2LjIzNC4xMDAuNDE6ODA4MC9lcm90aWMzL2luZGV4Lm0zdTg='
config_channel(name, url)
name='UElOSyBFUk9USUMgNA=='
url = 'aHR0cDovLzQ2LjIzNC4xMDAuNDE6ODA4MC9lcm90aWM0L2luZGV4Lm0zdTg='
config_channel(name, url)
name='SE9UIENMVUIgMQ=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYwOC5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgMg=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYwOS5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgMw=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxMC5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgNA=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxMS5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgNQ=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxMi5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgNg=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxMy5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgNw=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxNC5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgOA=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxNS5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgOQ=='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxNi5tM3U4'
config_channel(name, url)
name='SE9UIENMVUIgMTA='
url = 'aHR0cDovL3NlbGxpbmcwMS5kZG5zLm5ldDo4MDAwL2xpdmUvc2Ftc3VuZy9zYW1zdW5nLzYxNy5tM3U4'
config_channel(name, url)
name='UExBWUJPWSBSRUQgKEVTUCk='
url = 'aHR0cDovL2lwdHZsYXRpbm90b3RhbC4xNm1iLmNvbS9zdGFsa2VyLnBocD9jYW5hbD1QbGF5Ym95VFYmY209Mjg5JmY9Lm0zdTg='
config_channel(name, url)
name='WFRTWQ=='
url = 'aHR0cDovL2lwdHZsYXRpbm90b3RhbC4xNm1iLmNvbS9zdGFsa2VyLnBocD9jYW5hbD1YVFNZTEEmY209MTQ2MyZmPS5tM3U4'
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovLzIxMy4xMzYuNzMuNDEvODc0OC92ZW51cy5tM3U4'
config_channel(name, url)
name='UkVBTA=='
url = 'aHR0cDovL2lwdHZsYXRpbm90b3RhbC4xNm1iLmNvbS9zdGFsa2VyLnBocD9jYW5hbD1SZWFsTEEmY209MTAyMSZmPS5tM3U4'
config_channel(name, url)
name='U0VYVFJFTUU='
url = 'aHR0cDovL2lwdHZsYXRpbm90b3RhbC4xNm1iLmNvbS9zdGFsa2VyLnBocD9jYW5hbD1TZXh0cmVtZVNEJmNtPTI4NyZmPS5tM3U4'
config_channel(name, url)
name='SlVJQ1k='
url = 'aHR0cDovL2lwdHZsYXRpbm90b3RhbC4xNm1iLmNvbS9zdGFsa2VyLnBocD9jYW5hbD1KdWljeUxBJmNtPTEwMjMmZj0ubTN1OA=='
config_channel(name, url)
name='V09XIEdJUkxT'
url = 'aHR0cDovL2x1Y2t5aXB0di5kZG5zLm5ldDoyMzAwMC9saXZlL2x1ZG92aWNvL2x1ZG92aWNvLzkwMzIubTN1OA=='
config_channel(name, url)
name='QkFCRVM='
url = 'aHR0cDovL2x1Y2t5aXB0di5kZG5zLm5ldDoyMzAwMC9saXZlL2x1ZG92aWNvL2x1ZG92aWNvLzkwMTYubTN1OA=='
config_channel(name, url)

##############################################################################
xbmcplugin.endOfDirectory(addon_handle)