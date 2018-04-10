#change xml file path

import xml.etree.ElementTree as ET
import os

#打开trainval.txt
for line in open('trainval.txt'):
  if not os.path.exists('xmls/'+line.split(' ')[0]+'.xml'):
    print('%s is not exist'%line)
  else:
    tree=ET.parse('xmls/'+line.split(' ')[0]+'.xml')
    print("tree",tree)
    root=tree.getroot()
    name=root.find('filename')
    path=root.find('path')

    new_path=r'C:\Users\lele\Desktop\learn\data\annotations\xmls/'
    path.text=new_path+name.text

    tree.write('xmls/'+line.split(' ')[0]+'.xml')
