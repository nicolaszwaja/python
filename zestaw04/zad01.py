# . Zadanie ma na celu sprawdzenie jak wygląda tworzenie obiektów dla typów z wielokrotnym dziedziczeniem, 
# jakie funkcje __new__ oraz __init__ są lub nie są wywoływane. Wychodzimy od dwóch klas bazowych 
# (identycznych, różnią się tylko nazwą), class Baza(object) oraz class A(object) – patrz plik zadanie1.py. Posiadają 
# one napisane __new__, __init__, __str__ oraz funkcję id(). Proszę przestudiować kilka różnych wariantów klas 
# potomnych (B, C, D…) oraz tworzenia odpowiednich obiektów. Proponowane scenariusze są zapisane w pliku, 
# klasy potomne powinny mieć zawartość zbliżoną, w celach studyjnych, do klas bazowych. W programie 
# uruchomieniowym prezentować (oraz potrafić przedyskutować co się dzieje) różne scenariusze, włączając 
# zagadnienie MRO (Method Resolution Order).

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
        print("-> A __init__", x)
        super().__init__()
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

# SCENARIUSZ 1:
# print(B.mro())   # MRO dla klasy B - ['B', 'Baza', 'object']
# b = B(123)        # Wywołuje __new__ dla B, __new__ dla Baza, __init__ dla B, __init__ dla Baza
# print("------------")
# b.id()            # Wywołuje id() z B
# print("------------")
# print(b)          # Wywołuje __str__ z B

# SCENARIUSZ 2:
# print(C.mro())   # MRO dla klasy C - ['C', 'B', 'Baza', 'object']
# c = C(456)        # Wywołuje __new__ dla C, __new__ dla B, __new__ dla Baza, __init__ dla C, __init__ dla B, __init__ dla Baza
# print("------------")
# c.id()            # Wywołuje id() z C
# print("------------")
# print(c)          # Wywołuje __str__ z C

# SCENARIUSZ 3:
# print(D.mro())   # MRO dla klasy D - ['D', 'A', 'C', 'B', 'Baza', 'object']
# d = D(789)        # Wywołuje __new__ dla D, __new__ dla A, __new__ dla C, __new__ dla B, __new__ dla Baza,
#                   # __init__ dla D, __init__ dla A, __init__ dla C, __init__ dla B, __init__ dla Baza
# print("------------")
# d.id()            # Wywołuje id() z D
# print("------------")
# print(d)          # Wywołuje __str__ z D

# SCENARIUSZ 4:
# tak jak 3, tylko zobaczyć, co się dzieje podczas rzutowania:
# A(d).id() albo B(d),id() itp.
# Rzutowanie A(d).id() oznacza, że wykorzystuje metody z klasy A, bo jest pierwsza w MRO.
# Rzutowanie B(d).id() oznacza, że wykorzystuje metody z klasy B, bo jest pierwsza w MRO.

# d = D(789)        # Wywołuje __new__ i __init__ dla D, A, C, B, Baza
# a = A(d)          # Wywołuje __new__ i __init__ dla A
# b = B(d)          # Wywołuje __new__ i __init__ dla B, Baza
# print("------------")
# a.id()            # Wywołuje id() z A
# print("------------")
# b.id()            # Wywołuje id() z B
# print("------------")
