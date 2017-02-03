v = input()
v = v.split()
n1 = int(v[0])
n2 = int(v[1])
if n1 % n2 == 0 or n2 % n1 == 0:
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")
