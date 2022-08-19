"""
1) Сделайте предыдущее упражнение, но уже используя grid.
"""
from mod_set_win import *


o = window_setting()
l_1 = Label(o, text="Authorize")
l_2 = Label(o, text="Login")
l_3 = Label(o, text="Password")
t_l = Text(o, width=15, height=1)
t_p = Text(o,width=15, height=1)
b_1 = Button(o, text="Enter")

l_1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
l_2.grid(row=1, column=0, padx=5, pady=5)
l_3.grid(row=2, column=0, padx=5, pady=5)
t_l.grid(row=1, column=1, padx=5, pady=5)
t_p.grid(row=2, column=1, padx=5, pady=5)
b_1.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

o.mainloop()
