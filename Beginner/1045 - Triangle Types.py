v = input()
v = v.split()
n1 = float(v[0])
n2 = float(v[1])
n3 = float(v[2])
l = [n1, n2, n3]
l.sort()
a = l[2]
b = l[1]
c = l[0]
if a >= b + c:
	print("NAO FORMA TRIANGULO")
else:
	if a**2 == b**2 + c**2:
		print("TRIANGULO RETANGULO")
	if a**2 > b**2 + c**2:
		print("TRIANGULO OBTUSANGULO")
	if a**2 < b**2 + c**2:
		print("TRIANGULO ACUTANGULO")
	if a == b and a == c:
		print("TRIANGULO EQUILATERO")
	elif a == b or a == c or b == c:
		print("TRIANGULO ISOSCELES")
