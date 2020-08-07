#!/usr/bin/python3
#created by KIRILL SHVEDOV

import time

input()
print('Start! 00.00...')
startTime = time.time()
lastTime = startTime
print(lastTime)
lapNum = 1

try:
	while True:
		input()
		lapTime = round(time.time() - lastTime, 2)
		totalTime = round(time.time() - startTime, 2)
		print('Result #%s: %s, (%s)' %
			(lapNum, totalTime, lapTime), end ='')
		lapNum += 1
		lastTime = time.time()

except KeyboardInterrupt:
	print('\nDone.')

