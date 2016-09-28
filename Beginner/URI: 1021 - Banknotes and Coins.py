n = float(input())
centavos = n*100
n100 = int(n//100.0)
n %= 100
n50 = int(n//50.0)
n %= 50
n20 = int(n//20.0)
n %= 20
n10 = int(n//10.0)
n %= 10
n5 = int(n//5.0)
n %= 5
n2 = int(n//2.0)
n %= 2
n1 = int(n//1.0)
n %= 1
centavos %= 100
m50 = int(centavos//50)
centavos %= 50
m25 = int(centavos//25)
centavos %= 25
m10 = int(centavos//10)
centavos %= 10
m5 = int(centavos//5)
centavos %= 5
m1 = int(centavos)

print("NOTAS:\n{0} nota(s) de R$ 100.00\n{1} nota(s) de R$ 50.00\n{2} nota(s) de R$ 20.00".format(n100, n50, n20))
print("{0} nota(s) de R$ 10.00\n{1} nota(s) de R$ 5.00\n{2} nota(s) de R$ 2.00".format(n10, n5, n2))
print("MOEDAS:\n{0} moeda(s) de R$ 1.00\n{1} moeda(s) de R$ 0.50\n{2} moeda(s) de R$ 0.25".format(n1, m50, m25))
print("{0} moeda(s) de R$ 0.10\n{1} moeda(s) de R$ 0.05\n{2} moeda(s) de R$ 0.01".format(m10, m5, m1))
