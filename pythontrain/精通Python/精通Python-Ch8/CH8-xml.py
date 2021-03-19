# import xml.etree.ElementTree as et
# tree=et.ElementTree(file='menu.xml')
# root=tree.getroot()
# root.tag
# for child in root:
#     print('tag:', child.tag, 'attributes:',child.attrib)
#     for grandchild in child:
#         print('\ttag:',grandchild.tag,'attributes:',grandchild.attrib)

# print(len(root)) 
# print(len(root[0]))        
# import os
# print(os.getcwd())
menu =\
    {
    "breakfast":{
            "hour":"7-11",
            "items": {
                    "breakfast burritos":"$6.00",
                    "pancake":"$4.00"
                    }
            },
    "lunch": {
            "hour":"11-3",
            "items": {
                    "hamburger":"$5.00"
                    }
            },
    "dinner": {
            "hour":"3-10",
            "items": {
                    "spaghetti":"$8.00"
                    }
            }        
    }
    
import json
# menu_json= json.dumps(menu)
# print(menu_json)
# print("\n______________________________________________________")
# menu2 = json.loads(menu_json)
# print(menu2)

# import datetime
# now = datetime.datetime.utcnow()
# print(now)
# # json.dumps(now)
# now_str = str(now)
# print(json.dumps(now_str)) #要將datetime轉換成json，需要以字串或epoch值
# from time import mktime
# now_epoch = int(mktime(now.timetuple())) 
# print(json.dumps(now_epoch))

import yaml
with open('mcintyre.yaml', 'rt')as fin:
        text = fin.read()
data = yaml.load(text)
print(data['details'])
print(len(data['poems']))










