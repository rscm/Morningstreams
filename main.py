# -*- coding: utf-8 -*-
# This plugin is 3rd party and not part of plexus-streams addon
# Morningstreams
# http://morningstreams.com/

import sys
import os
import requests
from utils.webutils import *
from utils.pluginxbmc import *
from utils.directoryhandle import *

current_dir = os.path.dirname(os.path.realpath(__file__))
basename = os.path.basename(current_dir)
core_dir =  current_dir.replace(basename,'').replace('parsers','')
sys.path.append(core_dir)

# json format url
#[{"server":"Server 1","details":"Sky Sports F1 HD 1080p 6000kbps","id":"idhash1","acestreamid":"acehash1"},{"server":"Server 2","details":"Sky Sports F1 HD 720p 2000kbps","id":"idhash2","acestreamid":"acehash2"}]
#url = "http://138.197.183.39/api/acestreams"
url = "https://morningstreams.com/api/acestreams.json"

def module_tree(name,url,iconimage,mode,parser,parserfunction):
    if not parserfunction: ms_listing()


def ms_listing():
    try:
        r = requests.get(url)
        #TODO: On error, fallback to another url on urlList
        if r.status_code == 200: # exists
            j = r.json()
            for i in j:
                linkName = i["server"].encode("utf-8") + ": " + i["details"].encode("utf-8")
                linkUrl = i["acestreamid"].encode("utf-8")
                addDir(linkName,linkUrl, 1, os.path.join(current_dir,"icon.png"), 1, False)
        else:
            #TODO: Add codes and their messages / 301, 404, 403, etc
            # doesn't exist
            addDir("[B][COLOR red]<ERROR:" + str(r.status_code) + ">[/COLOR][/B] Can not access URL","#", 1, os.path.join(current_dir,"icon.png"), 1, False)
    except:
        #TODO: Check this
        xbmcgui.Dialog().ok(translate(40000),translate(40128))
        return
