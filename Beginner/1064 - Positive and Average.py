aux = 0
m = 0
for i in range(6):
	n = float(input())
	if n>0:
		m += n
		aux+=1
print("%d valores positivos\n%.1f" % (aux,m/aux))
