import time

x = 0
l1 = ['a', 'b', 'c']
z = '{}' #senha de  3 caracteis
y = ''
a = 'a'
while True:

	for s in l1:
		time.sleep(1)
		if len(y) == 0:
			y = s
		print(s)
	time.sleep(1)
	y += '{}'.format(y)
	print(y)
