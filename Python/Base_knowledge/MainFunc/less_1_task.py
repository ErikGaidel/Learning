"""
1) Выведите число, округлив его до 2 знаков после запятой.
2) Выведите с шагом в 1 градус все значения синуса угла от 0 до 180 градусов в таком виде:
«sin(УГОЛ_В_ГРАДУСАХ) = РЕЗУЛЬТАТ».
Примечание: разумеется, стоит использовать цикл.
"""

import random
from math import *

a = random.random()
print(a)
print(round(a, 2))

str_1 = "sin({degree}) = {value}"
for i in range(0, 181):
    v = round(sin(radians(i)), 4)
    print(str_1.format(degree=i, value=v))


