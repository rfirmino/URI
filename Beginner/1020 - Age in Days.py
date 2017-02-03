n = int(input())
a = n//365
m = (n%365)//30
d = n-365*a-30*m;
print("{0} ano(s)\n{1} mes(es)\n{2} dia(s)".format(a, m, d))
