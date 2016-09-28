n = int(input())
n100 = n//100;
n50 = (n-n100*100)//50;
n20 = (n-n100*100-n50*50)//20;
n10 = (n-n100*100-n50*50-n20*20)//10;
n5 = (n-n100*100-n50*50-n20*20-n10*10)//5;
n2 = (n-n100*100-n50*50-n20*20-n10*10-n5*5)//2;
n1 = n-n100*100-n50*50-n20*20-n10*10-n5*5-n2*2;
print("%d" % n)
print("%d nota(s) de R$ 100,00" % n100)
print("%d nota(s) de R$ 50,00" % n50)
print("%d nota(s) de R$ 20,00" % n20)
print("%d nota(s) de R$ 10,00" % n10)
print("%d nota(s) de R$ 5,00" % n5)
print("%d nota(s) de R$ 2,00" % n2)
print("%d nota(s) de R$ 1,00" % n1)
