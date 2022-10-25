import os
import toml
import msvcrt as mc
import easygui as eg
import base64 as b64
import requests
from pathlib import Path
from zipfile import ZipFile
config = open('config.toml', 'r').read()
config = toml.loads(config)
configM = config['Main']
config = config['DownloadProperties']

os.system('cls') # clears cmd :)

def yesOrNo():
    input = mc.getch()

    if input != b'y' and input != b'n':
        pass
    elif input == b'y':
        return False
    else:
        return "n"

logo = """              __        __               __          __ __ 
.--.--.-----.|__|______|__|.-----.-----.|  |_.---.-.|  |  |
|  |  |     ||  |______|  ||     |__ --||   _|  _  ||  |  |
|_____|__|__||__|      |__||__|__|_____||____|___._||__|__|
"""

# Menu
print(logo)
print("{}, by {}".format(configM['version'], configM['creator']))

print('\n\nDo you want to install %s? [y/n]' % config['program_name'])
Getching = True

while Getching:
    i = yesOrNo()

    if i == False:
        Getching = i
    elif i == "n":
        exit()

# Set path
if config['default_directory'] == "#d":
    defaultDir = str(Path.home() / "Downloads") + "\\"
elif config['default_directory'] == "#ad":
    defaultDir = str(Path.home() / "Appdata") + "\\"
else:
    defaultDir = config['default_directory']


print('Do you want to install it into the default directory? (%s) [y/n]' % (defaultDir + config['directory_folder']))
Getching = True

while Getching:
    i = yesOrNo()

    if i == False:
        directory = (config['default_directory'] + config['directory_folder'])
        Getching = False
    elif i == "n":
        directory = eg.diropenbox("Select a folder do you want to install %s" % config['program_name'])
        directory += '\\' + config['directory_folder']
        Getching = False
        
# print(directory)



# Downloading File
print('\n\nDownloading file(s)...  this can take some minutes (or hours)')

url = config['gdrive']
file_name = config['file_name']
directory += "\\"
url = b64.b64decode(url.encode("utf-8"))  # decoding because base64 utf-8

d_file = requests.get(url)  # gets file (content)
os.makedirs(directory, exist_ok=True)

open(directory + file_name, 'wb').write(d_file.content)  # write to the file (download)

# Check if is a zip and unpack
if config['is_zip']:
    with ZipFile(directory + file_name, 'r') as zip_ref:
        zip_ref.extractall(directory)

print('\nFinished!')

import subprocess
subprocess.Popen('explorer "%s"' % directory)

input('Press <Enter> to quit')