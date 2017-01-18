
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

name='LFhYWCB0YXRsb3YgbGVhZ3Vlcg=='
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9tb3ZpZS9tYW4vTUFOLzYxMDEubWt2'
config_channel(name, url)
name='RXR1ZGlhbnRlcy5JbmZpcm1pZXJlcy4xMDgw'
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9tb3ZpZS9tYW4vTUFOLzYxMTQubWt2'
config_channel(name, url)
name='aSBsb3ZlIG15IHNpc3RlcnNiaWcgdGl0cw=='
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9tb3ZpZS9tYW4vTUFOLzYxMjUubWt2'
config_channel(name, url)
name='V2lkZSBPcGVuIEhvdXNld2lmZS4xMDgwcA=='
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9tb3ZpZS9tYW4vTUFOLzYxMTAubWt2'
config_channel(name, url)
name='U0FGQURB'
url = 'aHR0cDovL3R2aGQuZHludS5jb206ODAwMC9tb3ZpZS9tYW4vTUFOLzYxMDgubWt2'
config_channel(name, url)
name='R2V0dGluZyBNZXNzeSBXaXRoIHRoZSBXaWZleQ=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4NzUubXA0'
config_channel(name, url)
name='SG93IFRvIE1hc3R1cmJhdGUgTGlrZSBBIFBvcm4gU3Rhcg=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4NzYubXA0'
config_channel(name, url)
name='SWYgWW91IEdvIERvd24gVG8gVGhlIFdvb2RzIFRvZGF5'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4NzcubXA0'
config_channel(name, url)
name='SmFpbCBob3VzZSBGdWNrIFR3bw=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4NzkubXA0'
config_channel(name, url)
name='SkFTTUlORSBUQU1FIEFGVEVSIFNDSE9PTCBMRVNTT04='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4NzgubXA0'
config_channel(name, url)
name='Sm9pbiBUaGUgTHVzdCBBcm15'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODAubXA0'
config_channel(name, url)
name='SnVzdCBHbyBGb3IgSXQ='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODEubXA0'
config_channel(name, url)
name='S0VOREFMTCBCUk9PS1MgU0tJUFBJTkcgQ0xBU1M='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODIubXA0'
config_channel(name, url)
name='S1JJU1RBTCBTVU1NRVJTIFRIRSBURUFDSEVSJ1MgUEVU'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODMubXA0'
config_channel(name, url)
name='S2FybWEgcyBhIEJpZyBCdXR0IEJpdGNo'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODQubXA0'
config_channel(name, url)
name='S2VycnkgTG91aXNlIGUgR3JhZGUgR3J1bm5pbmc='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODUubXA0'
config_channel(name, url)
name='S2lsZWUgU3RydXR0IEkgbG92ZSBzdWJzdGl0dXRlIHRlYWNoZXJz'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODYubXA0'
config_channel(name, url)
name='TEVaTEVZIFpFTiBNUy4gWkVOJ1MgU0lERSBKT0I='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODcubXA0'
config_channel(name, url)
name='TFVDS1kgQkVOVE9OIENVTSBPTiBCQUJZIExJR0hUIE1ZIEZJUkU='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODgubXA0'
config_channel(name, url)
name='TGFjZXkgRHV2YWxsZSBob3cgY29udmVuaWVudA=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4ODkubXA0'
config_channel(name, url)
name='TWFuaGFuZGxlZA=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4OTAubXA0'
config_channel(name, url)
name='TXkgU3RlcG1vbSdzIE5ldyBCb29icw=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4OTEubXA0'
config_channel(name, url)
name='Um91Z2ggVGltZSBGb3IgQSBUaW55IFRlYXNl'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4OTIubXA0'
config_channel(name, url)
name='U2l0IEFuZCBTcGlu'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4OTMubXA0'
config_channel(name, url)
name='U21vb3RoaWUgU2x1dA=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE4OTQubXA0'
config_channel(name, url)
name='QW5hbCBBdmVudWUgU2x1dHMgIzI='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NDgubXA0'
config_channel(name, url)
name='QW5hbCBCcmF0cyAy'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NDkubXA0'
config_channel(name, url)
name='QW5hbCBDcmF2aW5nIE1JTEZz'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NTAubXA0'
config_channel(name, url)
name='QW5hbCBDdXRpZXMgVm9sLiA0'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODEubXA0'
config_channel(name, url)
name='QW5hbCBGYW50YXN5'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5MzUubXA0'
config_channel(name, url)
name='QW5hbCBGb290YmFsbCBDbHVi'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODcubXA0'
config_channel(name, url)
name='QW5hbCBJbnRlcnZpZXdzICMy'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NTEubXA0'
config_channel(name, url)
name='QW5hbCBSb3lhbHR5'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NTIubXA0'
config_channel(name, url)
name='QW5pa2thJ3MgRnVjay1pdCBMaXN0IChEaXNjIDEp'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NTMubXA0'
config_channel(name, url)
name='QW5pa2thJ3MgRnVjay1pdCBMaXN0IChEaXNjIDIp'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NTQubXA0'
config_channel(name, url)
name='QmFieXNpdHRlcnMgUE9W'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5MjYubXA0'
config_channel(name, url)
name='QmFuZyBCdXMgVm9sLiA1OQ=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5MjgubXA0'
config_channel(name, url)
name='QmlnIEFuZCBCbGFjayAoRGlzYyAxKQ=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5OTMubXA0'
config_channel(name, url)
name='Rmlyc3QgUHJpbmNlICMz'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5MjUubXA0'
config_channel(name, url)
name='Rmxlc2ggLSBIb3VzZSBvZiBIZWRvbmlzbQ=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NDAubXA0'
config_channel(name, url)
name='RnVja2dpcmxzIChEaXNjIDEp'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjEubXA0'
config_channel(name, url)
name='RnVja2dpcmxzIChEaXNjIDIp'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjIubXA0'
config_channel(name, url)
name='RnVsbCBBbmFsIFNlcnZpY2UgIzI='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjMubXA0'
config_channel(name, url)
name='SGUgQ2FtZSBJbnNpZGUgTXkgSG90d2lmZSAjIDM='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5OTUubXA0'
config_channel(name, url)
name='SGUncyBJbiBDaGFyZ2UgMg=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NDYubXA0'
config_channel(name, url)
name='R2VybWFuIFRpdGxlIDE='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODgubXA0'
config_channel(name, url)
name='SG9va3VwIEhvdHNob3QgQmUgQSBTbHV0IERvIFdoYXRldmVyIFUgV2FudA=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjUubXA0'
config_channel(name, url)
name='SG9va3VwIEhvdHNob3QgU2xvYmJlciBEYW1hZ2U='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjYubXA0'
config_channel(name, url)
name='SG9ybnkgQ3Vja29sZCBCaXRjaGVz'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjcubXA0'
config_channel(name, url)
name='SG90IGFuZCBEaXJ0eSBUZWVucw=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5MzcubXA0'
config_channel(name, url)
name='SG90d2lmaW5nIChEaXNjIDEp'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODQubXA0'
config_channel(name, url)
name='SG90d2lmaW5nIChEaXNjIDIp'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5OTYubXA0'
config_channel(name, url)
name='SG93IEkgTG92ZSBNeSBTaXN0ZXI='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NzYubXA0'
config_channel(name, url)
name='SW5lcyAtIFByaXZhdGUgTnVyc2U='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODkubXA0'
config_channel(name, url)
name='SW5lcyBQcml2YXRsZWJlbiBlaW5lciBLcmFua2Vuc2Nod2VzdGVy'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5OTAubXA0'
config_channel(name, url)
name='SW5maWRlbGl0eQ=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NDEubXA0'
config_channel(name, url)
name='SW5rZWQgQW5nZWxzICM2'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjgubXA0'
config_channel(name, url)
name='SW50ZXJuYWwgRGFtbmF0aW9uIDEx'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODUubXA0'
config_channel(name, url)
name='SW50ZXJyYWNpYWwgQW5hbCBWb2wuIDI='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODIubXA0'
config_channel(name, url)
name='TGVzYmlhbiBGYW1pbHkgQWZmYWlyIDI='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NzcubXA0'
config_channel(name, url)
name='TWFudWVsJ3MgUE9WMiAtIEFsbCBBbmFs'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5ODMubXA0'
config_channel(name, url)
name='TW9uc3RlciBEaWNrIExpdHRsZSBXaGl0ZSBCaXRjaA=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NjkubXA0'
config_channel(name, url)
name='TW9uc3RlcnMgT2YgQ29jayBWb2wuIDYz'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5MzEubXA0'
config_channel(name, url)
name='TmFjaG8ncyBGaXJzdCBDbGFzcyBGdWNrcw=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NzAubXA0'
config_channel(name, url)
name='TmV0IFNraXJ0cyAxNA=='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NzgubXA0'
config_channel(name, url)
name='T2lsICYgQW5hbCAy'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NzEubXA0'
config_channel(name, url)
name='VGhlIFlvdW5nICYgVGhlIEJlYXV0aWZ1bCAzIChEaXNjIDIp'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5OTcubXA0'
config_channel(name, url)
name='VFMgRmFjdG9yIDQ='
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5NzQubXA0'
config_channel(name, url)
name='VWx0aW1hdGUgQmxvbmRlcyAy'
url = 'aHR0cDovL3NvbmljLnJldm9sdXRpb24ubnMwLml0OjI1NDYxL21vdmllL0x5UWhBRmp2NG8vdHJpbHV4LzE5MjcubXA0'
config_channel(name, url)



#############################################################################
xbmcplugin.endOfDirectory(addon_handle)