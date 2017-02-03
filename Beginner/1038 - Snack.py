v = input()
v = v.split()
x = int(v[0])
y = int(v[1])
if x == 1:
	t = 4.0*y
elif x == 2:
	t = 4.5*y
elif x == 3:
	t = 5.0*y
elif x == 4:
	t = 2.0*y
else:
	t = 1.5*y
print("Total: R$ %.2lf" % t)
