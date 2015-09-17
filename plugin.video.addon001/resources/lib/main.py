
import sys
import xbmcgui
import xbmcplugin

def config_channel(encoded_name,encoded_url, video=None, audio=None, subtitle=None):
	name = encoded_name.decode('base64')
	url = encoded_url.decode('base64')
	li = xbmcgui.ListItem(name, iconImage='DefaultVideo.png')
	if(video):
		li.addStreamInfo('video', video)
	if(audio):
		li.addStreamInfo('audio', audio)
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
	
addon_handle = int(sys.argv[1])
xbmcplugin.setContent(addon_handle, 'movies')

#####################paste links here ##################################################

name='VklFVC1TRVg='
url = 'cnRtcDovLzY0LjYyLjE0My41L2xpdmUvZG8lMjBub3QlMjBzdGVhbCUyMG15LVN0cmVhbTI='
config_channel(name, url)
name='WFhM'
url = 'aHR0cDovL2oubXAvWkNIX0MwM19YWExfc2x5'
config_channel(name, url)
name='QkxVRSBIVVNUTEVS'
url = 'aHR0cDovL2oubXAvWkNIX0MwM19CTFVFSFVTVExFUl9zbHk='
config_channel(name, url)
name='TWlhbWkgVFY='
url = 'aHR0cDovL2s0LnVzYXN0cmVhbXMuY29tOjE5MzUvbWlhbWl0di9zbWlsOm1pYW1pdHYvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='UGFzc2llWFhY'
url = 'cnRtcDovLzE3OC4zMy4xMjYuMjEzL2xldmVkLyBwbGF5UGF0aD1wYXNzaWVsaXZlc3RyZWFtIHN3ZlVybD1odHRwczovL3N0YXRpYy5yYW1wYW50LnR2L3N3Zi9wbGF5ZXIuc3dm'
config_channel(name, url)
name='UHJpdmF0ZQ=='
url = 'aHR0cDovLzE3OC4zMy4xMjYuMjEzOjE5MzUvbGV2ZWQvcHJpdmF0ZUNvbS8ubTN1OA=='
config_channel(name, url)
name='TlVBUlQ='
url = 'aHR0cDovLzgwLjc3LjUyLjY6MzcxOS91ZHAvMjI2LjAuNS42OjEyMzQ1'
config_channel(name, url)
name='VEVNUFRBVElPTg=='
url = 'aHR0cDovLzQ2LjE4Mi4yNS4zNDoxOTM1L3R2LzE0MjAvcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='UExBWUJPWQ=='
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi4yNDI6MTIzNA=='
config_channel(name, url)
name='WFhM'
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi43MjoxMjM0'
config_channel(name, url)
name='T0xBTEE='
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi45MDoxMjM0'
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVA=='
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi4xMDc6MTIzNA=='
config_channel(name, url)
name='UkVETElHSFQgSEQ='
url = 'aHR0cDovL3NlcnZlcjQuYmFsa2FudHZtZWRpYS5jb206ODA4MC9YWFgyP3U9dXNlcjgxMDpwPVRKbjBKU3lJ'
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzIxMy45NS40Ny4xMDQ6ODA4MC9idHZfMDAxODgv'
config_channel(name, url)
name='SFVTVExFUiBUVg=='
url = 'aHR0cDovL3NlcnZlcjQuYmFsa2FudHZtZWRpYS5jb206ODA4MC9YWFgzP3U9dXNlcjgxMDpwPVRKbjBKU3lJ'
config_channel(name, url)
name='TklHSFQgQ0xVQg=='
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi4zNzoxMjM0'
config_channel(name, url)
name='UFJJVkFURSBHT0xE'
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi4yMzE6MTIzNA=='
config_channel(name, url)
name='RlJFQ0hMT1ZFUg=='
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi41MDoxMjM0'
config_channel(name, url)
name='QlJBWlpFUlMgRVVST1BF'
url = 'aHR0cDovLzRCQTlFQkRCMDdDMDU4ODM6QDUuMTU5Ljk2LjE3MDo4MDAwL2JyYXp6ZXJz'
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovL3N0cmVhbWVyLnNpYmluZXQuY29tOjgwMDgvdWRwLzIzOS4yNTQuMi4yMjU6MTIzNA=='
config_channel(name, url)
name='UElOSyBFUk9USUM='
url = 'aHR0cDovL3NlcnZlcjkuYmFsa2FudHZtZWRpYS5jb206ODA4MC9YWFg0P3U9dXNlcjgxMDpwPVRKbjBKU3lJ'
config_channel(name, url)
name='UElOSyBFUk9USUMgMg=='
url = 'aHR0cDovL3NlcnZlcjQuYmFsa2FudHZtZWRpYS5jb206ODA4MC9YWFg1P3U9dXNlcjgxMDpwPVRKbjBKU3lJ'
config_channel(name, url)
name='UElOSyBFUk9USUMgMw=='
url = 'aHR0cDovL3NlcnZlcjQuYmFsa2FudHZtZWRpYS5jb206ODA4MC9YWFg2P3U9dXNlcjgxMDpwPVRKbjBKU3lJ'
config_channel(name, url)
name='UElOSyBFUk9USUMgNA=='
url = 'aHR0cDovL3NlcnZlcjkuYmFsa2FudHZtZWRpYS5jb206ODA4MC9YWFg3P3U9dXNlcjgxMDpwPVRKbjBKU3lJ'
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
name='Q2FtU29kYSBQb29sIFVuZGVyd2F0ZXI='
url = 'aHR0cDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1wb29sLXVuZGVyd2F0ZXIuc3RyZWFtL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='Q2FtU29kYSBDaGFybGV5IEhhcnQ='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6cnlhbmhhcnQ='
config_channel(name, url)
name='Q2FtU29kYSBCZWxsYSBTa3ll'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YmVsbGFza3lleHh4'
config_channel(name, url)
name='Q2FtU29kYSBSZWFnYW4gTW9ucm9l'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6cmVhZ2FubW9ucm9l'
config_channel(name, url)
name='Q2FtU29kYSBHaWEgUGFpZ2U='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6Z2lhcGFpZ2V4eHg='
config_channel(name, url)
name='Q2FtU29kYSBBZHJpYW4gTWF5YQ=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YWRyYWlubWF5YXh4eA=='
config_channel(name, url)
name='Q2FtU29kYSBHYWJyaWVsbGE='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6Z2FicmllbGxhMDA3'
config_channel(name, url)
name='Q2FtU29kYSBCcml0dGFueSBTaGFl'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YnJpdHRhbnlzaGFl'
config_channel(name, url)
name='Q2FtU29kYSBOYW9taSBXb29kcw=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bGlzc2Fwb2xvb3ph'
config_channel(name, url)
name='Q2FtU29kYSBEaWEgRGVsIFJvc2U='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6ZGlhZGVscm9zZQ=='
config_channel(name, url)
name='Q2FtU29kYSBNaXNzIExpbGxpIERpeG9u'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bWlzc2xpbGxpZGl4b24='
config_channel(name, url)
name='Q2FtU29kYSBNUyBGVUVHTw=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bXNmdWVnbw=='
config_channel(name, url)
name='Q2FtU29kYSBEZXN0aW55IExvdmU='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6ZGVzdGlueWxvdmU='
config_channel(name, url)
name='Q2FtU29kYSBLaW1iZXIgV29vZHM='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6ZGlhZGVscm9zZQ=='
config_channel(name, url)
name='Q2FtU29kYSBBbGFuYSBTcGljZQ=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YWxhbmFzcGljZQ=='
config_channel(name, url)
name='Q2FtU29kYSBJc2FiZWxsZSBMdXY='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6aXNhYmVsbGVsdXY='
config_channel(name, url)
name='Q2FtU29kYSBBZGVzc2EgV2ludGVycw=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YWRlc3Nhd2ludGVycw=='
config_channel(name, url)
name='Q2FtU29kYSBMdWN5IERvbGw='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bHVjeWRvbGw='
config_channel(name, url)
name='Q2FtU29kYSBDaGFybG90dGUgTydSeWFu'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6Y2hhcmxvdHRlb3J5YW4='
config_channel(name, url)
name='Q2FtU29kYSBMaWxseSBOYXVnaHR5'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bGlsbHluYXVnaHR5'
config_channel(name, url)
name='Q2FtU29kYSBIb2xseSBCZXJyeQ=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6aG9sbGllYmVycnk='
config_channel(name, url)
name='Q2FtU29kYSBIb3BlIEhhcnBlcg=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6aG9wZWhhcnBlcg=='
config_channel(name, url)
name='Q2FtU29kYSBQYW50aWUgUHJpbmNlc3M='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6cGFudGllcHJpbmNlc3M='
config_channel(name, url)
name='Q2FtU29kYSBHIFZhbGVudGluYQ=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6Z3ZhbGVudGluYXh4eA=='
config_channel(name, url)
name='Q2FtU29kYSBDcnlzdGFhbA=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6Y3J5c3RhYWw='
config_channel(name, url)
name='Q2FtU29kYSBDYWxsaWUgTmljb2xl'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6Y2FsbGllbmljb2xlODk='
config_channel(name, url)
name='Q2FtU29kYSBKYWRlIEJsYXpl'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6amFkZWJsYXpl'
config_channel(name, url)
name='Q2FtU29kYSBLeW1iZXJsZWVBbm5l'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6a3ltYmVybGVlYW5uZQ=='
config_channel(name, url)
name='Q2FtU29kYSBPdWxhbGFsYW5h'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6b3VsYWxhbGFuYQ=='
config_channel(name, url)
name='Q2FtU29kYSBHaWFubmEgTWljaGFlbHM='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6Z2lhbm5hbWljaGFlbHM0dQ=='
config_channel(name, url)
name='Q2FtU29kYSBEeW5hc3R5IEx1dg=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6ZHluYXN0eWx1dg=='
config_channel(name, url)
name='Q2FtU29kYSBXaWNrZWQgTHlubg=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6d2lja2VkbHlubg=='
config_channel(name, url)
name='Q2FtU29kYSBNaWxrc2hha2UgYW5kIE1yIFByb3Bz'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bWlsa3NoYWtl'
config_channel(name, url)
name='Q2FtU29kYSBTb2ZpZSBTdG9ybQ=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6c29maWVzdG9ybQ=='
config_channel(name, url)
name='Q2FtU29kYSBTb3BoaWEgTGVvbmU='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6c29waGlhbGVvbmUyMDE1'
config_channel(name, url)
name='Q2FtU29kYSBLZWxzaSBNb25yb2U='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6a2Vsc2ltb25yb2U='
config_channel(name, url)
name='Q2FtU29kYSBOaWNvbGUgQmV4bGV5'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bmljb2xlYmV4bGV5'
config_channel(name, url)
name='Q2FtU29kYSBBdmEgU2FuY2hleg=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YXZheHNhbmNoZXo='
config_channel(name, url)
name='Q2FtU29kYSBOYW9taSBXb29kcw=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bmFvbWl3b29kcw=='
config_channel(name, url)
name='Q2FtU29kYSBKZXdlbHM='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6amV3ZWxzeHh4'
config_channel(name, url)
name='Q2FtU29kYSBBbGFpbmEgS3Jpc3Rhcg=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YWxhaW5ha3Jpc3Rhcg=='
config_channel(name, url)
name='Q2FtU29kYSBOb2xsaWUgUm94eA=='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6bm9sbGllcm94eA=='
config_channel(name, url)
name='Q2FtU29kYSBBdmEgU3RlZWw='
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6YXZhc3RlZWw='
config_channel(name, url)
name='Q2FtU29kYSBTbm93IEJ1bm55'
url = 'cnRtcDovLzE5OS44OC41OS4yNDQ6MTkzNS9jYW0/dG9rZW49eHh4Lz9tcDQ6c25vdy1idW5ueQ=='
config_channel(name, url)

##############################################################################

xbmcplugin.endOfDirectory(addon_handle)