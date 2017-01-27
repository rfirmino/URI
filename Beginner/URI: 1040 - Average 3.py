v = input()
v = v.split()
n1 = float(v[0])
n2 = float(v[1])
n3 = float(v[2])
n4 = float(v[3])

media = (n1*2.0 + n2*3.0 + n3*4.0 + n4*1.0)/10.0

print("Media: %.1f" % media)

if media > 7.0:
	print("Aluno aprovado.")
elif media < 5.0:
	print("Aluno reprovado.")
else:
	print("Aluno em exame.")
	u = input()
	u = u.split()
	ne = float(u[0])
	print("Nota do exame: %.1lf" % ne)
	media2 = (media + ne)/2.0
	if media2 >= 5.0:
		print("Aluno aprovado.\nMedia final: %.1lf" % media2)
	else:
		print("Aluno reprovado.\nMedia final: %.1lf" % media2)
