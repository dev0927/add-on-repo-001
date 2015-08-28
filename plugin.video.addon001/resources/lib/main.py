
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
url = 'aHR0cDovL2ZlLW53LnN2Yy5pcHR2LnJ0LnJ1L2hscy9DSF9DMDNfWFhML3ZhcmlhbnQubTN1OD92ZXJzaW9uPTI='
config_channel(name, url)
name='QkxVRSBIVVNUTEVS'
url = 'aHR0cDovL2ZlLW53LnN2Yy5pcHR2LnJ0LnJ1L2hscy9DSF9DMDNfQkxVRUhVU1RMRVIvdmFyaWFudC5tM3U4P3ZlcnNpb249Mg=='
config_channel(name, url)
name='SE9U'
url = 'aHR0cDovLzQuMzEuMzAuMTU5OjkwMDM='
config_channel(name, url)
name='U0VYWk9ORQ=='
url = 'aHR0cDovLzYyLjIxMC44My4xODA6ODA4MS9zZXh6b25laGQvc2V4em9uZWhkL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='WFhYIE5FVw=='
url = 'aHR0cDovLzQuMzEuMzAuMTU5OjkwMDU='
config_channel(name, url)
name='UExBWUJPWSBUVg=='
url = 'aHR0cDovLzQuMzEuMzAuMTU5OjkwMDY='
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
name='UExBWUJPWQ=='
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuMjQyOjEyMzQ='
config_channel(name, url)
name='WFhM'
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuNzI6MTIzNA=='
config_channel(name, url)
name='T0xBTEE='
url = 'aHR0cDovLzQ2LjE4MS4yMzcuNzU6MTIzNC91ZHAvMjM5LjI1NS40Mi4yMTk6MTIzNA=='
config_channel(name, url)
name='UlVTU0lBTiBOSUdIVA=='
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuMTA3OjEyMzQ='
config_channel(name, url)
name='TklHSFQgQ0xVQg=='
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuMzc6MTIzNA=='
config_channel(name, url)
name='UFJJVkFURSBHT0xE'
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuMjMxOjEyMzQ='
config_channel(name, url)
name='UEVOVEhPVVNFIEhE'
url = 'aHR0cDovLzgyLjE0Ni4yMC45ODoxMjM0L3VkcC8yMzkuMTMwLjUwLjEyNDo5MDAx'
config_channel(name, url)
name='VEdJUkxT'
url = 'aHR0cDovLzgyLjE0Ni4yMC45ODoxMjM0L3VkcC8yMzkuMTMwLjUwLjEyNzo5MDAx'
config_channel(name, url)
name='U0FUSVNGQUNUSU9O'
url = 'aHR0cDovLzgyLjE0Ni4yMC45ODoxMjM0L3VkcC8yMzkuMTMwLjUwLjEyODo5MDAx'
config_channel(name, url)
name='U0NU'
url = 'aHR0cDovLzgyLjE0Ni4yMC45ODoxMjM0L3VkcC8yMzkuMTMwLjUwLjEyOTo5MDAx'
config_channel(name, url)
name='UElOS08gVFY='
url = 'aHR0cDovLzgyLjE0Ni4yMC45ODoxMjM0L3VkcC8yMzkuMTMwLjUwLjEzMDo5MDAx'
config_channel(name, url)
name='U0VYVE8gNiBTRU5TTw=='
url = 'aHR0cDovLzgyLjE0Ni4yMC45ODoxMjM0L3VkcC8yMzkuMTMwLjUwLjEyNjo5MDAx'
config_channel(name, url)
name='SFVTVExFUiBIRA=='
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuMjMyOjEyMzQ='
config_channel(name, url)
name='RlJFQ0hMT1ZFUg=='
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuNTA6MTIzNA=='
config_channel(name, url)
name='QlJBWlpFUlMgRVVST1BF'
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuMjQzOjEyMzQ='
config_channel(name, url)
name='Q0FORFk='
url = 'aHR0cDovLzg5LjI1MS43My4yMDo0MDIyL3VkcC8yMzkuMjU0LjIuMjI1OjEyMzQ='
config_channel(name, url)
name='VkVOVVM='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yNjE5LnRz'
config_channel(name, url)
name='RFVTSw=='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yMDY1LnRz'
config_channel(name, url)
name='UGxhdGludW0='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yNjMxLnRz'
config_channel(name, url)
name='RXhvdGljYQ=='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8xNzY5LnRz'
config_channel(name, url)
name='RG9yY2Vs'
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8xNzY4LnRz'
config_channel(name, url)
name='RGVzaXJl'
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yMDYxLnRz'
config_channel(name, url)
name='TWVpZGVuIHZvbiBIb2xsYW5kIEhhcmQ='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yMjk1LnRz'
config_channel(name, url)
name='QnVuZ2EgQnVuZ2E='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yMjk2LnRz'
config_channel(name, url)
name='UmVkbGlnaHQ='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8xNDg5LnRz'
config_channel(name, url)
name='QlJBU0lMRUlSSU5IQVM='
url = 'aHR0cDovLzYyLjIxMC44Mi4yNDE6ODA4MS9icmFzaWxlaXJpbmhhcy9icmFzaWxlaXJpbmhhcy9saXZlLm0zdTg='
config_channel(name, url)
name='QlJBU0lMRUlSSU5IQVMgMg=='
url = 'aHR0cDovLzYyLjIxMC44Mi4yNDE6ODA4MS9icmFzaWxlaXJpbmhhcy9icmFzaWxlaXJpbmhhczIvbGl2ZS5tM3U4'
config_channel(name, url)
name='UElOSyBFUk9USUM='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8zMzEzLnRz'
config_channel(name, url)
name='UElOSyBFUk9USUMgMg=='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yODg5LnRz'
config_channel(name, url)
name='UElOSyBFUk9USUMgMw=='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yODkwLnRz'
config_channel(name, url)
name='UElOSyBFUk9USUMgNA=='
url = 'aHR0cDovL2lwdHZjaG9pY2UuemFwdG8ub3JnOjgwMDAvbGl2ZS90ZXN0cmFwaWQvM0NtV0xmYjNrVy8yODkxLnRz'
config_channel(name, url)
name='Q2FtU29kYSBLaXRjaGVu'
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1raXRjaGVuLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBNYXN0ZXIgQmVkcm9vbSBB'
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1tYXN0ZXItYmVkcm9vbS1hLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBHYW1lIFJvb20='
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1nYW1lcm9vbS5zdHJlYW0vcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='Q2FtU29kYSBUaGF0IDcwcyBSb29t'
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS10aGF0NzBzcm9vbS5zdHJlYW0vcGxheWxpc3QubTN1OA=='
config_channel(name, url)
name='Q2FtU29kYSBNYXN0ZXIgQmVkcm9vbSBC'
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1tYXN0ZXItYmVkcm9vbS1iLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBCb29tYm9vbSBSb29t'
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1ib29tYm9vbS1yb29tLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBTaG93ZXI='
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1zaG93ZXIuc3RyZWFtL3BsYXlsaXN0Lm0zdTg='
config_channel(name, url)
name='Q2FtU29kYSBQb29s'
url = 'aHR0cDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW1ob3VzZS9jYW1ob3VzZS1wb29sLnN0cmVhbS9wbGF5bGlzdC5tM3U4'
config_channel(name, url)
name='Q2FtU29kYSBLZWVseSBKb25lcw=='
url = 'cnRtcDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW0/dG9rZW49NWJiNjg5YjQ2YTRmNWRhMzExOGEyYTA5OWQ3M2IyNWIvP21wNDprZWVseWpvbmVzIHN3ZlVybD1odHRwOi8vdmpzLnplbmNkbi5uZXQvNC4xMi92aWRlby1qcy5zd2YgcGFnZVVybD1odHRwOi8vd3d3LmNhbXNvZGEuY29tL2tlZWx5am9uZXMvY2hhdA=='
config_channel(name, url)
name='Q2FtU29kYSBSeWFuIEhhcnQ='
url = 'cnRtcDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW0/dG9rZW49ZDAxYmVlNWNhNDZhY2NjZDcxZmVmN2JjOGQxMTkzNTAvP21wNDpyeWFuaGFydCBzd2ZVcmw9aHR0cDovL3Zqcy56ZW5jZG4ubmV0LzQuMTIvdmlkZW8tanMuc3dmIHBhZ2VVcmw9aHR0cDovL3d3dy5jYW1zb2RhLmNvbS9yeWFuaGFydC9jaGF0'
config_channel(name, url)
name='Q2FtU29kYSBQZW5ueSBOaWNob2xz'
url = 'cnRtcDovL3ZpZDEuY2Ftc29kYS5jb206MTkzNS9jYW0/dG9rZW49YzYzY2RiMzAxMGFiNWVjODZhZmE4MDhhNjc3OGE3YzEvP21wNDpwZW5ueW5pY2hvbHMgc3dmVXJsPWh0dHA6Ly92anMuemVuY2RuLm5ldC80LjEyL3ZpZGVvLWpzLnN3ZiBwYWdlVXJsPWh0dHA6Ly93d3cuY2Ftc29kYS5jb20vcGVubnluaWNob2xzL2NoYXQ='
config_channel(name, url)

##############################################################################

xbmcplugin.endOfDirectory(addon_handle)