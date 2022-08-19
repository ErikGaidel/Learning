"""
1) Создайте окно с меткой, где должно выводиться случайное целое число от 1 до 1000.
Примечание: то есть при каждом запуске программы там должно появляться случайное число.
"""
from mod_set_win import *
from random import random

o = window_setting()
d = int(random()*1000 + 1)
lab_1 = Label(o, text="Your random digit is {0}!".format(d), bg="#ff0c0c", font="Tahoma 18", fg="white")
lab_1.pack()
print(type(o))
o.mainloop()
