# !/usr/bin/python3
# created by Kirill Shvedov 
# github: "LosGnidoS"

import re 

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
x = regex.search('My phone number\
 is 123-343-9999')
print('Phone number found: ' + x.group())