import sys
from urlparse import parse_qsl
from pbr_resolver import pbr_resolver
import xbmcgui
import xbmcplugin

# Get the plugin url in plugin:// notation.
_url = sys.argv[0]
# Get the plugin handle as an integer number.
addon_handle = int(sys.argv[1])


#TODO parse _url for params????


#TODO Add singly now but would be more efficient to add all at once with addDirectoryItems instead reconfigure how items identified/stored See example plugin 
def add(encoded_name, encoded_url, resolver=None, thumb=None, fanArt=None, title=None):
         # Example: plugin://plugin.video.example/?action=play&video=http://www.vidsplay.com/vids/crab.mp4
    name = encoded_name.decode('base64')
    url = encoded_url.decode('base64')
    url = '{0}?action=play&resolver={2}&video={1}'.format(_url, url, resolver)
   
    # Create a list item with a text label 
    list_item = xbmcgui.ListItem(label=name)
    #TODO Finish the extra bells and whistles
    '''        
    # Set a fanart image for the list item.
    # Here we use the same image as the thumbnail for simplicity's sake.
    list_item.setProperty('fanart_image', video['thumb'])
    # Set additional info for the list item.
    list_item.setInfo('video', {'title': video['name'], 'genre': video['genre']})
    # Set additional graphics (banner, poster, landscape etc.) for the list item.
    # Again, here we use the same image as the thumbnail for simplicity's sake.
    list_item.setArt({'landscape': video['thumb']})
    # Set 'IsPlayable' property to 'true'.
    # This is mandatory for playable items!
    list_item.setProperty('IsPlayable', 'true')
    # Create a URL for the plugin recursive callback.
    # Add the list item to a virtual Kodi folder.
    # is_folder = False means that this item won't open any sub-list.
    is_folder = False
    '''
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item)


def play(name,streamurl,iconimage = "DefaultVideo.png"):
	#streamurl += ' timeout=15'
	liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
	'''
	liz.setInfo('video', {'Title': name })
	liz.setProperty('IsPlayable', 'true')
	liz.setPath(path=streamurl)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]),True,liz)
	'''
	player = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
	player.play(streamurl,liz)
	
#from example
def play_video(path):
    if debug :
        print(path)
        return
   # Create a playable item with a path to play.
    play_item = xbmcgui.ListItem(path=path)
    # Pass the item to the Kodi player.
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem=play_item)
    
    
def create_list():    
    xbmcplugin.setContent(addon_handle, 'movies')
    
    ## add channels
    add('TWlhbWkgVFY=','aHR0cDovL2s0LnVzYXN0cmVhbXMuY29tOjE5MzUvbWlhbWl0di9zbWlsOm1pYW1pdHYvcGxheWxpc3QubTN1OA==')

    
    xbmcplugin.endOfDirectory(addon_handle)

def router(paramstring):
    
    	# Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))
    # Check the parameters passed to the plugin
    if params:
        url = params['video']
        if params['action'] == 'play':
            # Play a video from a provided URL.
            if params['resolver']!= None:
                url = locals()[params['resolver']](url)
            play_video(url)
        #elif params['action'] == 'listing':
            	#For future *pages*
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of videos
        create_list()


if __name__ == '__main__':
	# Call the router function and pass the plugin call parameters to it.
	# We use string slicing to trim the leading '?' from the plugin call paramstring
	router(sys.argv[2][1:])
    
    