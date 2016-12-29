import os
import re
import sys
import urllib

import xbmc
import xbmcgui
import xbmcaddon
import xbmcplugin

from resources.lib.chaturbate import Chaturbate

from urlparse import parse_qsl
from doctest import UnexpectedException
#from pbr_resolver import pbr_resolver


# Get the plugin url in plugin:// notation.
addon_url = sys.argv[0]

# Get the plugin handle as an integer number.
addon_handle = int(sys.argv[1])

def add(model):

    url = '{0}?action=play&model={1}'.format(addon_url, model['name'])
   
    # Create a list item with a text label 
    list_item = xbmcgui.ListItem(label=model['name'], iconImage=model['image'])
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item)


def play(model, url):
    liz = xbmcgui.ListItem(model)
    '''
    liz.setInfo('video', {'Title': name })
    liz.setProperty('IsPlayable', 'true')
    liz.setPath(path=streamurl)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]),True,liz)
    '''
    player = xbmc.Player(xbmc.PLAYER_CORE_AUTO)
    player.play(url,liz)
    
def create_menu(v):    
        categories = v.get_categories()
        
        items = []
        for category in categories:
            url = sys.argv[0] + "?" + urllib.urlencode({
                'category' : category,
                'page' : 1
            })
            item = xbmcgui.ListItem(category)
            items.append((url, item, True))
        xbmcplugin.addDirectoryItems(addon_handle, items)
        xbmcplugin.endOfDirectory(addon_handle)
        xbmc.executebuiltin("Container.SetViewMode(500)")


def create_list(v, category="Female", page=0):    

    models = v._get_models_on_page(category,page)
    for model in models:
        add(model)
    #add next page item
    if(v.on_last_page() == False):
        url = sys.argv[0] + "?" + urllib.urlencode({
                    'category' : category,
                    'page' : int(page) + 1})
        list_item = xbmcgui.ListItem("Next Page", iconImage='DefaultFolder.png')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=list_item, isFolder=True)
    xbmcplugin.endOfDirectory(addon_handle)
    xbmc.executebuiltin("Container.SetViewMode(500)")

def router(paramstring):
#    v = ModelCache()
    v = Chaturbate()
        # Parse a URL-encoded paramstring to the dictionary of
    # {<parameter>: <value>} elements
    params = dict(parse_qsl(paramstring))

    # Check the parameters passed to the plugin
    if params:
        if 'action' in params and params['action']!= None and params['action']!='None':
            if params['action'] == 'play':
                # Play a video from a provided URL.
                if 'model' in params and params['model']!= None and params['model']!='None':
                    print params['model']
                    play(params['model'],v.get_model_media(params['model']))
        elif 'category' in params and params['category']!= None and params['category']!='None':
            if 'page' in params and params['page']!= None and params['page']!='None':
                create_list(v, params['category'], params['page'])
            else:
                create_list(v, params['category'])
        else:
            raise UnexpectedException(params)        
    else:
        # If the plugin is called from Kodi UI without any parameters,
        # display the list of videos
        create_menu(v)


if __name__ == '__main__':
    # Call the router function and pass the plugin call parameters to it.
    # We use string slicing to trim the leading '?' from the plugin call paramstring
    router(sys.argv[2][1:])
    