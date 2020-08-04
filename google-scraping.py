#!/usr/bin/python3
#created by KIRILL SHVEDOV
#github: "LosGnidoS"


'''SIMPLE AUTOMATIZATION SCRIPT
FOR GOOGLE-MAPS SEARCH'''

#1.CTRL-C SOME ADDRESS YOU WANT TO REACH
#2.RUN THIS SCRIPT

import webbrowser, sys, pyperclip
if len(sys.argv) > 1 :
	address = ''.join(sys.argv[1:])

address = pyperclip.paste()
webbrowser.open('https://www.google.com/maps/place/'\
		+ address)

