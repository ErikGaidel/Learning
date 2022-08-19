"""
1) Сделайте у класса из предыдущего упражнения закрытыми все его поля.
2) Добавьте методы get и set для всех полей. Поскольку полей всего 4, то должно быть 4 метода get и 4 метода set.
3) Убедитесь, что доступа к полям уже нет за пределами класса.
4) Проверьте работу методов get и set.
5) Сделайте закрытый метод printlog(), в котором с помощью функции print() выводите значение переданного параметра.
6) В методах get и set вызывайте метод printlog с параметром: «Запрошено свойство NAME» (для методов get) или
«Изменено свойство NAME» (для методов set). Вместо NAME должно быть подставлено имя соответствующего свойства.
"""





class Rectangle:
    __x = 0
    __y = 0
    __w = 0
    __h = 0

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self):
        return "Прямоугольник с координатами (" + str(self.x) + ";" + str(self.y) + ') шириной ' + str(self.w) + " и высотой " + str(self.h) + ". "

    def getx(self):
        self.__printlog("Запрошено свойство X")
        return self.x

    def gety(self):
        self.__printlog("Запрошено свойство Y")
        return self.y

    def getw(self):
        self.__printlog("Запрошено свойство W")
        return self.w

    def geth(self):
        self.__printlog("Запрошено свойство H")
        return self.h

    def setx(self, x):
        self.__printlog("Изменено свойство X")
        self.x = x

    def sety(self, y):
        self.__printlog("Изменено свойство Y")
        self.y = y

    def setw(self, w):
        self.__printlog("Изменено свойство W")
        self.w = w

    def seth(self, h):
        self.__printlog("Изменено свойство H")
        self.h = h

    def square(self):
        return self.h * self.w

    def perimeter(self):
        return 2*(self.h + self.w)

    def __printlog(self, p):
        print(p)


r = Rectangle(1, 1, 1, 1)
print(r)
r.x = 10
#  r.__printlog() this is private method
r.setx(10)
print(r.getx())
r.sety(10)
print(r.gety())
r.seth(10)
print(r.geth())
r.setw(10)
print(r.getw())
print(r)
print(r.square())
print(r.perimeter())
