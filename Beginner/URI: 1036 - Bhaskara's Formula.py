v = input()
v = v.split()
a = float(v[0])
b = float(v[1])
c = float(v[2])
if b*b - 4.0*a*c < 0 or a == 0:
	print("Impossivel calcular")
else:
	r1 = (-b + (b*b - 4.0*a*c)**(1/2))/(2.0*a)
	r2 = (-b - (b*b - 4.0*a*c)**(1/2))/(2.0*a)
	print("R1 = %.5lf\nR2 = %.5lf" % (r1, r2))
