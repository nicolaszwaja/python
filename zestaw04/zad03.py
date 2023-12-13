# podpunkt A)
class A(object):
    def foo(self, x):
        print(f"wykonanie foo({self}, {x})")

    @classmethod
    def class_foo(cls, x):
        print(f"class_foo({cls}, {x})")

    @staticmethod
    def static_foo(x):
        print(f"wykonanie static_foo({x})")

a = A()
a.foo(123)       # Wywołanie metody instancji, wykonanie foo(<__main__.A object at ...>, 123)
A.foo(a, 123)    # To samo co powyższe, można używać na klasie, ale przekazywać instancję ręcznie
a.class_foo(123) # Wywołanie metody klasy, class_foo(<class '__main__.A'>, 123)
A.class_foo(123) # To samo co powyższe, można używać na klasie, ale przekazywać klasę ręcznie
a.static_foo(123)# Wywołanie metody statycznej, wykonanie static_foo(123)
A.static_foo(123)# To samo co powyższe, można używać na klasie, ale przekazywać klasę ręcznie

# podpunkt B)
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class Child1(Base):
    def abstract_method(self):
        print("Implementacja w Child1")

class Child2(Base):
    def abstract_method(self):
        print("Implementacja w Child2")

# Test
obj1 = Child1()
obj1.abstract_method()  # Wywołanie zaimplementowanej metody abstrakcyjnej w Child1

obj2 = Child2()
obj2.abstract_method()  # Wywołanie zaimplementowanej metody abstrakcyjnej w Child2

# podpunkt C)
class MyClass:
    _my_attribute = None  # Prywatny atrybut

    @property
    def my_attribute(self):
        # print("pobieranie wartości")
        return self._my_attribute

    @my_attribute.setter
    def my_attribute(self, value):
        # print("ustawianie wartości")
        self._my_attribute = value

# Test
obj = MyClass()
obj.my_attribute = 42     
value = obj.my_attribute       
print(value)# Wyświetlenie: 42
