from math import lcm, gcd


class Fraction:

    def __init__(self, num, denom):
        self.numerator = num
        self.denomenator = denom

    def __simple(self):
        grchdel = gcd(self.numerator, self.denomenator)
        self.numerator //= grchdel
        self.denomenator //= grchdel
        return self

    def __add__(self, *args):
        if len (args) == 1:
            other = args[0]
            if isinstance (other, int):
                sum = Fraction (self.numerator + other * self.denomenator, self.denomenator)
            else:
                if self.denomenator != other.denomenator:
                    sum = Fraction (self.numerator * other.denomenator + self.denomenator * other.numerator,
                                    self.denomenator * other.denomenator)
                else:
                    sum = Fraction (self.numerator + other.numerator, self.denomenator)
            return sum.__simple()
        sum = self
        for i, name in enumerate(args):
            sum = sum + name
        return sum.__simple()

    def __sub__(self, *args):
        if len (args) == 1:
            other = args[0]
            if isinstance (other, int):
                sub = Fraction (self.numerator - other * self.denomenator, self.denomenator)
            else:
                if self.denomenator != other.denomenator:
                    sub = Fraction (self.numerator * other.denomenator - self.denomenator * other.numerator,
                                    self.denomenator * other.denomenator)
                else:
                    sub = Fraction (self.numerator - other.numerator, self.denomenator)
            return sub.__simple()
        sub = self
        for i, name in enumerate (args):
            sub = sub - name
        return sub.__simple()

    def __mul__(self, *args):
        if len (args) == 1:
            other = args[0]
            if isinstance (other, int):
                mult = Fraction (self.numerator * other, self.denomenator)
            else:
                mult = Fraction (self.numerator * other.numerator, self.denomenator * other.denomenator)
            return mult.__simple()
        mult = self
        for i, name in enumerate (args):
            mult = mult * name
        return mult.__simple()

    def __truediv__(self, *args):
        if len (args) == 1:
            other = args[0]
            if isinstance (other, Fraction):
                other.denomenator, other.numerator = other.numerator, other.denomenator
                div = self * other
            else:
                div = Fraction(self.numerator, self.denomenator * other)
            return div.__simple()
        div = self
        for i, name in enumerate (args):
            div = div / name
        return div.__simple()

    def __int__(self):
        return self.numerator // self.denomenator

    def __float__(self):
        return self.numerator / self.denomenator

    def __str__(self):
        return f"Fraction {self.numerator}/{self.denomenator}"


class OperationsOnFraction (Fraction):

    def getint(self):
        return int (self)

    def getfloat(self):
        return float (self)


a = OperationsOnFraction (16, 3)
n = [Fraction(1,2), 1, Fraction(1,10), 3]
s = [
    Fraction (1, 10) + Fraction (1, 10) + 3 + 1 + Fraction (1, 10) + 1,
    Fraction (1, 2) * Fraction (1, 2) * 16,
    Fraction (2, 8) - Fraction (1, 10) - 1 - 2,
    int (Fraction (8, 3)),
    float (Fraction (8, 3)),
    Fraction (1, 2) / Fraction (1, 4) / 2,
    a,
    a.getint (),
    a.getfloat ()
]
a = a.__add__(*n)
print(a)
a = a.__sub__(*n)
print(a)
a = a.__mul__(*n)
print(a)
a = a.__truediv__(*n)
print(a)
print()

print(*s)
for w in s:
    print (w)
