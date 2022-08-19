"""
1) Выведите чекбокс, который при каждом запуске программы случайным образом должен быть либо включенным, либо выключенным.
"""
from mod_set_win import *
import random

o = window_setting()
ch = IntVar()
ch.set(int(round(random.random())))
check = Checkbutton(o, text="Something u wanna", variable=ch, onvalue=1, offvalue=0)
#  check.select()
#  check.deselect()
print(ch.get())
check.pack()
o.mainloop()

