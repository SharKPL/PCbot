# from settings.meta_engine import get_engine
import json
import os

# engine = get_engine()
# conn = engine.connect()

if os.path.isfile("settings/coms.txt"):
    coms = json.loads(open("settings/coms.txt", "r").read())
else:
    #coms = [{"": ""}, {"": ""}, {"": ""}]
    coms = []

if os.path.isfile("settings/data.txt"):
    dat = json.loads(open("settings/data.txt", "r").read())
else:
    dat = {"API": "", "ID": 0}

if os.path.isfile("settings/coms_list.txt"):
    coms_list = json.loads(open("settings/coms_list.txt", "r").read())
else:
    coms_list = {}

keys = []
for d in coms:
    if d != {'': ''}:
        keys.append(list(d.keys())[0])

closkeys = []
for i in keys:
    closkeys.append(str(i)+" закрыть")


try:
    TOKEN = dat["API"]
    
    user = int(dat["ID"])
   
except:
    raise SystemExit('нет данных')

path = "photo/screen.png"
#path_img = "imgs/nya.png"

