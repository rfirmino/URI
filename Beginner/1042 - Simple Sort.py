v = input()
v = v.split()
n1 = int(v[0])
n2 = int(v[1])
n3 = int(v[2])
l1 = [n1, n2, n3]
l1.sort()
print("%d\n%d\n%d\n\n%d\n%d\n%d" % (l1[0],l1[1],l1[2],n1,n2,n3))
