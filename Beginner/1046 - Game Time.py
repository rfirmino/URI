v = input()
v = v.split()
n1 = int(v[0])
n2 = int(v[1])
if n1 >= n2:
	n3 = 24 - n1 + n2
else:
	n3 = n2 - n1
print("O JOGO DUROU %d HORA(S)" % n3)
