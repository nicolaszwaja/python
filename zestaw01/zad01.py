# Napisać program, który czyta podane jako zewnętrzne argumenty liczby naturalne, a następnie każdą 
# rozkłada na czynniki pierwsze (co polega na zapisaniu dowolnej liczby naturalnej za pomocą iloczynu 
# liczb pierwszych). Wymagany jest format wyjściowy w postaci a1^k1*a2^k2*…*a3, jeśli ki==1 to 
# opuszczamy wykładnik potęgi

import sys

def rozklad_na_czynniki_pierwsze(n):
    czynniki = []
    dzielnik = 2
    while n > 1:
        if n % dzielnik == 0:
            czynniki.append(dzielnik)
            n //= dzielnik
        else:
            dzielnik += 1
    return czynniki

def formatuj_wyjscie(n, czynniki):
    wynik = ""
    czynnik = czynniki[0]
    licznik = 1
    for i in range(1, len(czynniki)):
        if czynniki[i] == czynnik:
            licznik += 1
        else:
            if licznik == 1:
                wynik += str(czynnik) + "*"
            else:
                wynik += str(czynnik) + "^" + str(licznik) + "*"
            czynnik = czynniki[i]
            licznik = 1
    if licznik == 1:
        wynik += str(czynnik)
    else:
        wynik += str(czynnik) + "^" + str(licznik)
    
    print(f"{n} = {wynik}")

argv = sys.argv[1:] # argv to lista, a 1: robi selekcje bez pierwszego argumentu – nazwy programu
if len(argv) < 1:
    print("Podaj co najmniej jedną liczbę jako argument.")
else:
    for i in range(1, len(argv)):
        n = int(sys.argv[i])
        czynniki = rozklad_na_czynniki_pierwsze(n)
        formatuj_wyjscie(n, czynniki)