"""
1) Создайте список из 5-ти значений с названиями городов.
2) Выведите радиокнопки с этими названиями городов, используя цикл по списку.
Примечание: для параметра variable создайте отдельную переменную и её значением должен быть индекс списка. То есть,
если в списке город «Москва» имеется индекс 3, то и value при создании радио-кнопки должен быть равен 3.
"""
from mod_set_win import *


o = window_setting()
l_1 = ["Moscow", "Minsk", "Brest", "Saint-Petersburg", "Berlin"]
lab = Label(o, text="Choose your city")
lab.pack()
choice = IntVar()

for c in l_1:
    r = Radiobutton(o, text=c, variable=choice, value=l_1.index(c))
    r.pack()
choice.set(3)
o.mainloop()
