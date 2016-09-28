v = input()
v = v.split()
a = int(v[0])
b = int(v[1])
c = int(v[2])
MaiorAB = (a+b+abs(a-b))/2;
MaiorABC = (MaiorAB+c+abs(MaiorAB-c))/2;
print("%d eh o maior" % MaiorABC)
