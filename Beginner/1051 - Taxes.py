v = input()
v = v.split()
s = float(v[0])
if s <= 2000:
	print("Isento")
elif s <= 3000:
	ir = 0.08*(s-2000)
	print("R$ %.2lf" % ir)
elif s <= 4500:
	ir = 80 + 0.18*(s-3000)
	print("R$ %.2lf" % ir)
elif s > 4500:
	ir = 80 + 18*15 + 0.28*(s-4500)
	print("R$ %.2lf" % ir)
