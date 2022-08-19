"""
1) Попросите пользователя ввести 3 числа: год, месяц и число рождения.
2) Напишите ему, сколько секунд он уже живёт.
"""
from datetime import *
from time import *

bdy = input("Enter year when u are born: ")
bdm = input("Enter month when u are born: ")
bdd = input("Enter day when u are born: ")

bd = datetime(int(bdy), int(bdm), int(bdd))
print(bd)
sec = bd.timestamp()
cd = datetime.today()
print(cd)
sec_1 = cd.timestamp()
sec_2 = sec_1 - sec
print("U lived ", sec_2, "sec!")


