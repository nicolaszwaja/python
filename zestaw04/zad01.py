class Baza(object):
    def __new__(cls, *args):
        print("-> Baza __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- Baza __new__")
        return nowy_obiekt
    def __init__(self, x):
        print("-> Baza __init__", x)
        super().__init__()
        print("-- Baza __init__")
        self.x = x
        print("<- Baza __init__")
    def __str__(self):
        return "{self.x}".format(self=self)
    def id(self):
        print("-Baza-")

class A(object):
    def __new__(cls, *args):
        print("-> A __new__", *args)
        nowy_obiekt = object.__new__(cls)
        print("<- A __new__")
        return nowy_obiekt
    def __init__(self, x):
        print("-> A __init__",x)
        super().__init__(x)
        print("-- A __init__")
        self.x = x
        print("<- A __init__")
    def __str__(self):
        return "{self.x}".format(self=self)
    def id(self):
        print("-A-")


class B(Baza):
    pass

class C(B):
    pass

class D(A, C, B, Baza):
    # tu nie definiować __new__
    pass

### SCENARIUSZ 1: 
print("SCENARIUSZ 1: ")
# print(B.mro())
#  Wyświetla kolejność dziedziczenia dla klasy B, używając metody MRO (Method Resolution Order).
#  [<class '__main__.B'>, <class '__main__.Baza'>, <class 'object'>]
# b = B(123)
#  Tworzy obiekt klasy B, co prowadzi do wywołania __new__ i __init__ dla klasy B.
# print("------------")
# b.id()
#  Wywołuje metodę id() zdefiniowaną w klasie Baza (klasa nadrzędna klasy B).
# print("------------")
# print(b)
#  Wywołuje metodę __str__ zdefiniowaną w klasie B.

### SCENARIUSZ 2: 
# print("SCENARIUSZ 2: ")
# print(C.mro())
# c = C(456)
# print("------------")
# c.id()
# print("------------")
# print(c)
# Podobnie jak SCENARIUSZ 1, ale dla klasy C.


### SCENARIUSZ 3: 
print("SCENARIUSZ 3: ")
# print(D.mro())
# d = D(789)
# print("------------")
# d.id()
# print("------------")
# print(d)

### SCENARIUSZ 4: 
# tak jak 3, tylko zobaczyć, co się dzieje podczas rzutowania:
# A(d),id() albo B(d),id() itp.

