"""
1) Создайте список из 3-х элементов, где значениями будут 3 различных цвета.
2) При наведении курсора мыши на окно программы (именно на окно) цвет его фона должен меняться на случайный элемент
 из списка, созданного в предыдущем пункте.
3) При уводе курсора мыши с окна программы цвет его фона должен возвращаться на цвет по умолчанию.
"""
from mod_set_win import *
from random import random

o = window_setting()
l_1 = ["green", "blue", "red"]


def handler_enter(event):
    r = int(random()*3)
    event.widget.config(bg=l_1[r])


def handler_leave(event):
    event.widget.config(bg="white")


but_1 = Button(text="First", bg="white", font="Tahoma 20")
but_2 = Button(text="Second", bg="white", font="Tahoma 20")

but_1.bind("<Enter>", handler_enter)
but_1.bind("<Leave>", handler_leave)
but_2.bind("<Enter>", handler_enter)
but_2.bind("<Leave>", handler_leave)

but_1.pack()
but_2.pack()

o.mainloop()
