v = input()
v = v.split()
s = float(v[0])
if s >= 0 and s <= 400:
	ns = s*1.15
	rg = ns - s
	ep = "15 %"
	print("Novo salario: %.2lf\nReajuste ganho: %.2lf\nEm percentual: %s" % (ns,rg,ep))
elif s >= 400.01 and s <= 800:
	ns = s*1.12
	rg = ns - s
	ep = "12 %"
	print("Novo salario: %.2lf\nReajuste ganho: %.2lf\nEm percentual: %s" % (ns,rg,ep))
elif s >= 800.01 and s <= 1200:
	ns = s*1.10
	rg = ns - s
	ep = "10 %"
	print("Novo salario: %.2lf\nReajuste ganho: %.2lf\nEm percentual: %s" % (ns,rg,ep))
elif s >= 1200.01 and s <= 2000:
	ns = s*1.07
	rg = ns - s
	ep = "7 %"
	print("Novo salario: %.2lf\nReajuste ganho: %.2lf\nEm percentual: %s" % (ns,rg,ep))
elif s >= 2000:
	ns = s*1.04
	rg = ns - s
	ep = "4 %"
	print("Novo salario: %.2lf\nReajuste ganho: %.2lf\nEm percentual: %s" % (ns,rg,ep))
