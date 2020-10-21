#Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2  Date de ieşire  medie_poz=13.66  medie_neg=-3.33.
i=0
n=0
m=0
sum_poz=0
sum_neg=0
while i<12:
    temperatura=eval(input("introduceti temperatura intro luna"))
    if temperatura>=0:
        sum_poz+=temperatura
        n+=1
    if temperatura<0:
        sum_neg+=temperatura
        m+=1
    i=i+1

    if n>0:
        media_poz=float(sum_poz/n)
        print("media pozitiva este:", med_poz) 

    if m>0:
        media_neg=float(sum_neg)
        print("media negativa:", med_neg)