# Dyskutowane w zadaniu poprzednim rozwiązania mają pewne ograniczenia, jest to nowa funkcjonalność 
# w języku Python, która nadal nie obejmuje bardziej skomplikowanych zastosowań (np. przypadków 
# dziedziczenia). W tym zadaniu przyjrzymy się zewnętrznemu modułowi multipledispatch

from multipledispatch import dispatch

class Figura(object):
    def __init__(self):
        print("Figura init")

class Prostokat(Figura):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

class Kwadrat(Prostokat):
    def __init__(self, x):
        super().__init__(x, x)

@dispatch(Figura)
def pole(instance: Figura):
    print("Pole: Figura")
    return 0

@dispatch(Prostokat)
def pole(instance: Prostokat):
    print("Pole: Prostokat")
    return instance.x * instance.y

@dispatch(Prostokat, int, int)
def pole(instance: Prostokat, x, y):
    instance.x = x
    instance.y = y
    return instance.x * instance.y

@dispatch(Kwadrat)
def pole(instance: Kwadrat):
    print("Pole: Kwadrat")
    return instance.x * instance.x

@dispatch(Kwadrat, int)
def pole(instance: Kwadrat, x):
    instance.x = x
    return instance.x * instance.x

# Test cases
a, b, c = Figura(), Prostokat(2, 4), Kwadrat(2)

bb = pole(b)
print(bb)

cc = pole(c)
print(cc)

def polaPowierzchni(listaFigur):
    for i in listaFigur:
        print(pole(i))

polaPowierzchni([a, b, c])
