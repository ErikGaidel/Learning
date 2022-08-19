"""
1) Сделайте кнопку с текстом «Сгенерировать случайное число».
2) При клике по кнопке под ней должно появляться случайное целое число от 1 до 100.
Примечание: для вывода сгенерированного числа используйте Label.
"""
from mod_set_win import *
from random import random

o = window_setting()


def click():
    rand_digit = int(random() * 100)
    l_1 = Label(o, text=rand_digit, font="Tahoma 20")
    l_1.grid(row=0, column=2)


b_1 = Button(o, text="Generate random digit", font="Tahoma 15", command=click)

b_1.grid(row=0, column=0)
o.mainloop()

