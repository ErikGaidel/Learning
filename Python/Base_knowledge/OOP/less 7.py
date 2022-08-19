"""
1) Сделайте класс автомобиля из предыдущего упражнения абстрактным.
2) Сделайте метод движения у этого класса так же абстрактным.
3) Создайте ещё один дочерний класс от класса автомобиля для ещё какой-нибудь конкретной модели и
реализуйте абстрактный метод движения.
"""
from abc import ABC, abstractmethod


class Car(ABC):
    x = 0
    y = 0
    s = 0
    w = 0

    def __init__(self, x, y, s, w):
        self.x = x
        self.y = y
        self.s = s
        self.w = w

    @abstractmethod
    def move(self):
        pass


class BigCar(Car):
    c = 0

    def __init__(self, x, y, s, w, c):
        Car.__init__(self, x, y, s, w)
        self.c = c

    def move(self, x, y):
        self.x = x
        self.y = y
        print("Big car moved to " + str(self.x) + ", " + str(self.y))


class PremCar(Car):
    r = 0

    def __init__(self, x, y, s, w, r):
        Car.__init__(self, x, y, s, w)
        self.r = r

    def move(self, x, y):
        self.x = x
        self.y = y
        print("Prem car moved to " + str(self.x) + ", " + str(self.y))


b = BigCar(0, 0, 90, 3, 2)
b.move(12, 12)
print(b.c)
c = PremCar(0, 0, 200, 1, 0)
c.move(25, 25)
