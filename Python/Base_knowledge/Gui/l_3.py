"""
1) Посмотрите в справочнике, какие есть параметры у Button.
2) Добавьте несколько кнопок с различными значениями атрибутов в окно.
"""
from mod_set_win import *


o = window_setting()
but_1 = Button(o, text="one", bg="white", cursor="wait")
but_2 = Button(o, text="two", bg="yellow")
but_3 = Button(o, bg="blue", text="three", fg="white")

but_1.pack()
but_2.pack()
but_3.pack()
o.mainloop()