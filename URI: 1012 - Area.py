v = input()
v = v.split()
a = float(v[0])
b = float(v[1])
c = float(v[2])
tri = (a*c)/2.0;
circ = 3.14159*c*c;
trap = (a+b)*c/2.0;
quad = b*b;
ret = a*b;
print("TRIANGULO: %.3lf" % tri)
print("CIRCULO: %.3lf" % circ)
print("TRAPEZIO: %.3lf" % trap)
print("QUADRADO: %.3lf" % quad)
print("RETANGULO: %.3lf" % ret)
