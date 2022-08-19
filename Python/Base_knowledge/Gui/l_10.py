"""
1) Создайте 3 элемента Frame.
2) В первый Frame добавьте label с текстом «Важная форма».
3) Во второй Frame добавьте 2 текстовых поля.
4) В третий Frame добавьте кнопку «Отправить форму».
5) Разместите все 3 элемента Frame в окне.
"""
from mod_set_win import *


o = window_setting()

frame_1 = Frame(o, bd=5, bg="red")
frame_2 = Frame(o, bd=5, bg="blue")
frame_3 = Frame(o, bd=5, bg="green")
lab = Label(frame_1, text="Important form")
tex_1 = Text(frame_2)
tex_2 = Text(frame_2)
button = Button(frame_3, text="Send form")
frame_1.pack()
frame_2.pack()
frame_3.pack()
lab.pack()
tex_1.pack()
tex_2.pack()
button.pack()
o.mainloop()
