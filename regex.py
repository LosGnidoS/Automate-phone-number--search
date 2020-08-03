# !/usr/bin/python3
# created by Kirill Shvedov 
# github: "LosGnidoS"


# SIMPLE REGEX SCRIPT HOW TO FIND
#ALL NUMBERS AND E-MAILS IN THE COPIED TEXT

import re 
import pyperclip

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? #area code
	(\s|-|\.)? #spaces
	(\d{3}) #first 3 figures
	(\s|-|\.)? #spaces
	(\d{4}) # second 4 figures
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9.-]+
	(\.[a-zA-Z] {2,4})
	)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for group in phoneRegex.findall(text):
	s = '-'
	phoneNum = s.join([group[1],\
		group[3], group[5]])
	if group[8] != '':
		phoneNum += ' x' + group[8]
	matches.append(phoneNum)

for group in emailRegex.findall(text):
	matches.append(group[0])


if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied successfully:')
	print('\n'.join(matches))
else:
	print('Nothing found')
