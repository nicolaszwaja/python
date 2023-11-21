# Dla dowolnego podanego łańcucha znakowego wypisać: ile jest w nim słów (poprzez słowo rozumiemy ciąg co najmniej jednego znaku innego niż znak przestankowy, dla uproszczenia przyjmijmy, że liczymy a-z, 
# A-Z i 0-9 jako coś, co składa się na słowa), ile liter, ile cyfr, oraz wypisać statystykę częstości występowania poszczególnych liter oraz cyfr

import string

def analizuj_łańcuch(łańcuch):
    licznik_słów = 1
    licznik_liter = 0
    licznik_cyfr = 0
    częstość_liter = {}
    częstość_cyfr = {}

    for znak in łańcuch:
        if znak.isalpha():
            licznik_liter += 1
            litera = znak.lower()
            częstość_liter[litera] = częstość_liter.get(litera, 0) + 1
        elif znak.isdigit():
            licznik_cyfr += 1
            częstość_cyfr[znak] = częstość_cyfr.get(znak, 0) + 1
        elif znak in string.punctuation:
            continue
        else:
            licznik_słów += 1

    print("liczba słów:", licznik_słów)
    print("liczba liter:", licznik_liter)
    print("liczba cyfr:", licznik_cyfr)

    print("\nStatystyka częstości występowania liter:")
    for litera, licznik in częstość_liter.items():
        print(f"{litera}: {licznik}")

    print("\nStatystyka częstości występowania cyfr:")
    for cyfra, licznik in częstość_cyfr.items():
        print(f"{cyfra}: {licznik}")

test1 = "sprawdzam 123 czy dziala 456"
analizuj_łańcuch(test1)


