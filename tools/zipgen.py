# Script to generate the zip files required for <datadir zip="true"> in the
# addon.xml of a repository

import os
import xml.etree.ElementTree
from zipfile import ZipFile


def get_plugin_version(addon_dir):
    addon_file = os.path.join(addon_dir, 'addon.xml')
    if(not os.path.exists(addon_file)) :
        #not an addon directory
        return
    try:
        data = open(addon_file, 'r').read()
        node = xml.etree.ElementTree.XML(data)
        return(node.get('version'))
    except Exception as e:
        print ('Failed to open %s' % addon_file)
        print( e.message)

def create_zip_file(fpath, addon):
    print("addon_dir: " + addon)
    version = get_plugin_version(os.path.join(fpath,addon))
    if not version:
        return
    print("version: " + version)
    home = os.getcwd();
    os.chdir(fpath)
    with ZipFile(addon + os.sep + addon + '-' + version + '.zip','w') as addonzip:
        for root, dirs, files in os.walk(addon):
            print("Root: " + root )
            print("Dirs: " + str(len(dirs)) )
            print("Files: " + str(len(files)) )
            for file_path in files:
                if file_path.endswith('.zip'):
                    continue
                print ("adding %s" % os.path.join(root, file_path)) 
                addonzip.write(os.path.join(root, file_path))
        addonzip.close()

    os.chdir(home)
def main(fpath):
    fpath = fpath or  "."
    print("fpath in zipgen:" + fpath)
    dirs = (os.listdir(fpath))
    print(str(len(dirs)) + " dirs found in zipgen")
    for addon_dir in dirs:
        directory = os.path.join(fpath, addon_dir)
        if(not os.path.isdir(directory)):
            continue      
        if(addon_dir.startswith('.')):
            # skip hidden dirs
            continue
        ## does noting at the mnment
        if(addon_dir.startswith("download")):
            # skip download directory
            continue
        
        print("processing..." + addon_dir)
        create_zip_file(fpath, addon_dir)

if __name__ == '__main__':
    main()