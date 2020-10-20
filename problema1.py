#Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse. Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14.
n=1
suma=1
while ((n>0)and(n!=0)):
    suma+=n
    n=eval(input("introduceti un numar: "))

print("suma numerelor este: ",suma)