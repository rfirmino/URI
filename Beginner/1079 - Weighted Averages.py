n = int(input())
for i in range(n):
	v = input()
	v = v.split()
	n1 = float(v[0])
	n2 = float(v[1])
	n3 = float(v[2])
	media = (n1*2 + n2*3 + n3*5)/10
	print("%.1f" % media)
