v = input()
v = v.split()
n1 = float(v[0])
n2 = float(v[1])
n3 = float(v[2])
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
	p = n1 + n2 + n3
	print("Perimetro = %.1lf" % p)
else:
	a = ((n1 + n2)*n3)/2
	print("Area = %.1lf" % a)
