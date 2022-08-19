"""
1) В цикле попросите пользователя вводить названия городов, каждый раз добавляя их в список.
2) Когда пользователь введёт 0, то нужно выйти из цикла.
3) Используя созданный список, выведите его с помощью Listbox в окно программы.
"""
from mod_set_win import *

inp = 1
l_1 = list()
while True:
    inp = input("Enter the city name or 0 to end entering: ")
    if inp == "0":
        break
    l_1.append(inp)

o = window_setting()
l_b = Listbox(o, font="Tahoma 20", width=20, height=10, selectmode=MULTIPLE)
for i in l_1:
    l_b.insert(END, i)

l_b.pack()
o.mainloop()
