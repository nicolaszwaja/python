# Napisać funkcję odwracanie(L, left, right) odwracającą kolejność elementów na liście od numeru left do
# right włącznie. Lista jest modyfikowana w miejscu (in place). Rozważyć wersję iteracyjną i rekurencyjną
# Wersja iteracyjna

def odwracanie_it(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

# Wersja rekurencyjna
def odwracanie_rek(L, left, right):
    if left < right:
        L[left], L[right] = L[right], L[left]
        odwracanie_rek(L, left + 1, right - 1)

# przykład
lista = [1, 2, 3, 4, 5, 6]
lewy_indeks = 1
prawy_indeks = 4

odwracanie_it(lista, lewy_indeks, prawy_indeks)
print("Wersja iteracyjna:", lista)

lista = [1, 2, 3, 4, 5, 6]
odwracanie_rek(lista, lewy_indeks, prawy_indeks)
print("Wersja rekurencyjna:", lista)
