#Elaborați un program care va calcula suma, produsul și media aritmetică a numerelor de la 1 la n, pentru n introdus de la tastatură.
n=eval(input('Introduceti un numar:'))
c=0
suma=0
produsul=1

while c<n:
    c+=1
    suma+=c
    produsul*=c

print(f'Suma={round(suma, 2)}', f'Produsul={round(produsul, 2)}', f'Media aritmetica={round(suma/c, 2)}', sep='\n')
