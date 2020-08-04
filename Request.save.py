#!usr/bin/python3
#created by KIRILL SHVEDOV

'''SIMPLE AUTOMATIZATION SCRIPT
FOR WEB-SCRAPING'''

#1.FIND NEEDED WEB-SITE
#2.JUST CTRL-C URL()
#3.CHANGE FILE'S NAME('NameFile.txt')

import requests, pyperclip

url = pyperclip.paste()
res = requests.get(url)

res.raise_for_status()

saveFile = open('NameFile.txt', 'wb')

for byte in res.iter_content(100000):
	saveFile.write(byte)


saveFile.close()