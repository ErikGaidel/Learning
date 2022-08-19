"""
1) Попросите пользователя ввести путь к картинке.
2) Следующим шагом попросите его указать, с каким масштабом выводить изображение.
3) Выведите его в окно программы с указанным пользователем масштабированием, используя Label.
Примечание: нужно учесть, что, если пользователь вводит значения меньше 1, значит, он хочет его сжать,
и для этого потребуется функция subsample, а также перевод, например, 0.2 в число 5 (1 / 0.2).
"""
from mod_set_win import *

o = window_setting()

p = input("Please, enter the path to image: ")
s = float(input("Please select the scale that u needed: "))
ph = PhotoImage(file=p)
if s < 1:
    m = int(round(1/s))
    bg_ph = ph.subsample(m, m)
else:
    m = int(round(s))
    bg_ph = ph.zoom(m, m)

im = Label(o, image=bg_ph)
im.pack()
o.mainloop()
