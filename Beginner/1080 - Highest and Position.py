l = []
for i in range(100):
	n = int(input())
	l.append(n)
print("%d\n%d" % (max(l),l.index(max(l))+1))
