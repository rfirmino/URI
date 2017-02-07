n = int(input())
if 10000 % n == 0:
	y = int(10000/n)
else:
	y = int(10000/n) + 1
for i in range(0,y):
	print("%d" % (n*i + 2))
