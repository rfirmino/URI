n = int(input())
c = 0
r = 0
s = 0
for i in range(n):
	v = input()
	v = v.split()
	q = int(v[0])
	if v[1] == 'C':
		c += q
	elif v[1] == 'R':
		r += q
	else:
		s += q
t = c + r + s
p = '%'
print("Total: %d cobaias\nTotal de coelhos: %d\nTotal de ratos: %d\nTotal de sapos: %d\nPercentual de coelhos: %.2f %s\nPercentual de ratos: %.2f %s\nPercentual de sapos: %.2f %s"
 % (t,c,r,s,100.0*c/t,p,100.0*r/t,p,100.0*s/t,p))
