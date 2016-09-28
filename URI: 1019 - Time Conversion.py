n = int(input())
h = n//3600
m = (n%3600)//60
s = n%60
print("{0}:{1}:{2}".format(h, m, s))
