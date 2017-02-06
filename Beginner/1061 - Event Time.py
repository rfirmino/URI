v1 = input()
v1 = v1.split()
d1 = int(v1[1])
i1 = input()
i1 = i1.split(' : ')
h1 = int(i1[0])
m1 = int(i1[1])
s1 = int(i1[2])
v2 = input()
v2 = v2.split()
d2 = int(v2[1])
i2 = input()
i2 = i2.split(' : ')
h2 = int(i2[0])
m2 = int(i2[1])
s2 = int(i2[2])

d = d2 - d1
h = h2 - h1
m = m2 - m1
s = s2 - s1

if h < 0:
	h += 24
	d -= 1
if m < 0:
	m += 60
	h -= 1
if s < 0:
	s += 60
	m -= 1
	
print("%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)" % (d,h,m,s))
