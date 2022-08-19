"""
1) Создайте текстовое поле.
2) Попросите пользователя ввести в консоли произвольную строку.
3) Выведите эту строку в текстовом поле окна.
Примечание: запрос строки и её вывод в текстовом поле должны происходить до mainloop().
"""
from mod_set_win import *


o = window_setting()
entry_1 = Entry(o, bg="yellow", font="Tahoma 20")
t = input("Enter the text u wanna see in window:")
print(type(t))
entry_1.insert(END, t)
entry_1.pack()
o.mainloop()
