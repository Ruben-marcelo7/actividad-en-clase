P = input ("ingresa la palabra: ")
if str(P) == str(P) [:: -1]:
    print("es un palindromo")
else:
    print("no es un palindromo")

P_R = ""

for L in P:
  P_R = P_R + L

if P == P_R:
    print("es un palindromo")
else:
    print("no es un palindromo")
    