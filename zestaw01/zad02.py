# Napisać program rysujący "miarkę" o zadanej długości. Należy prawidłowo obsłużyć liczby składające 
# się z kilku cyfr (ostatnia cyfra liczby ma znajdować się pod znakiem kreski pionowej). Należy zbudować 
# pełny string, a potem go wypisać.

dlugosc = 20
dlugosc = int(input("Podaj dlugosc miarki: "))
liczba_cyfr = len(str(dlugosc))

odleglosc = ""
for i in range(0,liczba_cyfr):
    odleglosc += " ."

miarka = odleglosc
rozmiar = len(odleglosc) 
      
for i in range(1,dlugosc):
    miarka += "|" + odleglosc
miarka += "|\n"

for i in range(1,dlugosc+1):
    miarka += (rozmiar-len(str(i))+1)*" "
    miarka += str(i)

print(miarka)


