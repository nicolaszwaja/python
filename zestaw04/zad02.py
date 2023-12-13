# Szkielet kodu klasy Zespolona. Posiada ona dwie składowe 
# instancji, r (real) oraz i (imaginary), odpowiadające części rzeczywistej i urojonej liczby zespolonej. Dodatkowo 
# zdefiniowane są funkcje sprzężenia zespolonego (conjugate) oraz fazy (argz). Reszta to szereg metod specjalnych 
# __NNN__, których treść (w miejsce pass) należy napisać tak, żeby nastąpiło poprawne wykonanie kodu w funkcji 
# main() – oczekiwane wyniki zapisano w komentarzu

from math import hypot, atan, sin, cos

class Zespolona:
    def __init__(self, r, i):
        self.r = r  #część rzeczywista
        self.i = i  #część urojona

    # sprzężenie zespolone
    def conjugate(self):
        return self.__class__(self.r, -self.i)

    # faza
    def argz(self):
        return atan(self.i / self.r)

    def __abs__(self):
        return hypot(self.r, self.i)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.r}, {self.i})"

    def __str__(self):
        if self.i < 0:
            return f"({self.r}{self.i}j)"
        elif self.i == 0:
            return f"({self.r})"
        return f"({self.r}+{self.i}j)"


    def __add__(self, other):
        if isinstance(other, self.__class__):
            real = self.r + other.r
            imag = self.i + other.i
        else:
            real = self.r + other
            imag = self.i

        return self.__class__(real, imag)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            real = self.r - other.r
            imag = self.i - other.i
        else:
            real = self.r - other
            imag = self.i
        return self.__class__(real, imag)

    # (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
    # (a + bi) * c = ac + bci
    def __mul__(self, other):
        if isinstance(other, self.__class__):
            real = self.r * other.r - self.i * other.i
            imag = self.r * other.i + self.i * other.r
        else:
            real = self.r * other
            imag = self.i * other

        return self.__class__(real, imag)

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -self + other

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.r == other.r and self.i == other.i
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.r != other.r or self.i != other.i
        else:
            return True

    def __neg__(self):
        return Zespolona(-self.r, -self.i)

    # z^n = r^n * (cos(n*argz) + i*sin(n*argz)) 
    def __pow__(self, other):
        if isinstance(other, int):
            r = abs(self)
            r_pow = r**other
            real = round(cos(other * self.argz()) * r_pow)
            imag = round(sin(other * self.argz()) * r_pow)

            return self.__class__(real, imag)
        else:
            raise ValueError("Exponent must be an integer")


def main():
    print("Liczby zespolone")
    a = Zespolona(2, 5)
    b = Zespolona(1, -3)
    print(a)
    print(b)
    b_copy = eval(repr(b))
    print(type(b_copy), b_copy.r, b_copy.i)
    print(a + b)
    print(a - b)
    print(a + 4)
    print(7 - a)
    print(a * 4)
    print(a * (-4))
    print(a == Zespolona(2, 5))
    print(a == b)
    print(a != b)
    print(a != Zespolona(2, 5))
    print(a**2)
    print(b**4)


if __name__ == "__main__":
    main()


# Liczby zespolone
# (2+5j)
# (1-3j)
# <class '__main__.Zespolona'> 1 -3
# (3+2j)
# (1+8j)
# (6+5j)
# (5-5j)
# (8+20j)
# (-8-20j)
# True
# False
# True
# False
# (-21+20j)
# (28+96j)