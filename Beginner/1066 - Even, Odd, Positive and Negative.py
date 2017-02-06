par = 0
impar = 0
pos = 0
neg = 0
for i in range(5):
	n = float(input())
	if n > 0:
		pos += 1
	elif n < 0:
		neg += 1
	if n%2 == 0:
		par+=1
	elif n%2 != 0:
		impar += 1
print("%d valor(es) par(es)\n%d valor(es) impar(es)\n%d valor(es) positivo(s)\n%d valor(es) negativo(s)" % (par,impar,pos,neg))
