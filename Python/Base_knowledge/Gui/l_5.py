"""
1) Создайте текстовый файл с произвольным текстом.
2) Выведите текстовую область в окно, где должен быть выведен весь текст из файла, созданном в предыдущем пункте.
Примечание: разумеется, надо воспользоваться функциями для работы с файлами.
"""
from mod_set_win import *

file = open("file.txt","a")
file.write("ngfhnsdavhqaovhoaihnvgah")
file.close()

o = window_setting()
text = Text(o, width=30, height=10, font="Tahoma 30", bd=3)

file = open("file.txt")
buf = file.read()
file.close()

text.insert(END, buf)
text.pack()
o.mainloop()
