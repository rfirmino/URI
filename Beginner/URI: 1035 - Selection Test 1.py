v = input()
v = v.split()
a = int(v[0])
b = int(v[1])
c = int(v[2])
d = int(v[3])
if b > c and d > a and c + d > a + b and c > 0 and d > 0 and not(a&1):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")
