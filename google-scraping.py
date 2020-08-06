#!/usr/bin/python3
#google-scraping.py
#created by KIRILL SHVEDOV

'''OPENS FIRST FEW LINKS 
AFTER SEARCHING IN GOOGLE'''

import requests, bs4, webbrowser, sys, pyperclip


print('Processing...')

address = pyperclip.paste()
if len(sys.argv) > 1 :
	address = ''.join(sys.argv[1:])
res = requests.get("https://www.google.\
	com/search?q=" + address)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text,\
	"html.parser")

linkElems = soup.select('.r a')
print(len(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open("http://google.com"\
	 + linkElems[i.get('href')])





