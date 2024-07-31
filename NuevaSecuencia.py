N = int(input("ingrese un numero: "))
NL = range(1,N +1)
NE = " "
for l in NL:
    NE += str(l) + " "
print (NE)
print (str (NE) [::-1])