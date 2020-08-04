#!usr/bin/python3
#created by KIRILL SHVEDOV

'''SIMPLE AUTOMATIZATION SCRIPT
FOR WEB-SCRAPING'''

#1.FIND NEEDED WEB-SITE
#2.COPY,PAST URL
#

import requests, pyperclip

url = pyperclip.paste()
res = requests.get(url)

res.raise_for_status()

saveFile = open('RomeoAndJuliet.txt', 'wb')

for byte in res.iter_content(100000):
	saveFile.write(byte)


saveFile.close()