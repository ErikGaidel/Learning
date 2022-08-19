"""
1) Сделайте 4 элемента Label, задав у них одинаковые параметры width и height.
2) Выведите первый Label вверху по центру, второй и третий слева и справа соответственно под первым элементом,
а четвёртый по центру снизу.
"""
from mod_set_win import *


o = window_setting()
l_1 = Label(o, width=10, height=5, text="Label 1", bg="red")
l_2 = Label(o, width=10, height=5, text="Label 2", bg="blue")
l_3 = Label(o, width=10, height=5, text="Label 3", bg="yellow")
l_4 = Label(o, width=10, height=5, text="Label 4", bg="green")

l_1.pack(side="top")
l_2.pack(side="left", anchor="e")
l_3.pack(side="right")
l_4.pack(side="bottom", expand=True, anchor="s")

o.mainloop()
