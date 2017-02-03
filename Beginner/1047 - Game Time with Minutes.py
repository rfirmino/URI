v = input()
v = v.split()
h1 = int(v[0])
m1 = int(v[1])
h2 = int(v[2])
m2 = int(v[3])
h3 = h2 - h1
m3 = m2 - m1
if h3 <= 0:
	h3 += 24
	if m3 < 0:
		m3 += 60
		h3 -= 1
else:
	if m3 < 0:
		m3 += 60
		h3 -= 1
print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h3,m3))
