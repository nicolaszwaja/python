# Mamy trzy liczby całkowite, x, y, zreprezentujące wymiary prostopadłościanu, oraz pewną liczbę naturalną 
# n. Wypisz listę wszystkich możliwych współrzędnych (i, j, k) na trójwymiarowej siatce, gdzie i+j+k 
# nie jest równe n. 

x = int(input("podaj wartość x: "))
y = int(input("podaj wartość y: "))
z = int(input("podaj wartość z: "))
n = int(input("podaj wartość n: "))

wyniki = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                wyniki.append([i, j, k])
            
print(wyniki)            
            