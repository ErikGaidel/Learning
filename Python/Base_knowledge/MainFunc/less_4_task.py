"""
1) Создайте 2 множества, состоящие из 10 случайных целых чисел от 1 до 10 (включая 1 и 10).
2) Выведите 3 множества: объединением этих двух множеств, их разницей и их пересечением.
"""
import random

set_1 = set(int(random.random()*10)+1 for i in range(0, 11))
print(set_1)
set_2 = set(int(random.random()*10)+1 for i in range(0, 11))
print(set_2)
set_3 = set_1.union(set_2)
set_4 = set_1.difference(set_2)
set_5 = set_1.intersection(set_2)
print(set_3)
print(set_4)
print(set_5)
