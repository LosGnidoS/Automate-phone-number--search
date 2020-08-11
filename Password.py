import random

lower = "abcdefghijklmnopqrstuvwxyz" 
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
numbers = "0123456789" 
symbols = "[]{}()*;/,._-"

all_lists = lower + upper + numbers + symbols

lenght = 16

password = "".join(random.sample(all_lists, lenght))

print(password)