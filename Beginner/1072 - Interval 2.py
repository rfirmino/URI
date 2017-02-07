n = int(input())
dentro = 0
fora = 0
for i in range(n):
	x = int(input())
	if x <= 20 and x >= 10:
		dentro += 1
	else:
		fora += 1
print("%d in\n%d out" % (dentro,fora))
