"""
1) Используя place, создайте форму входа со следующими элементами: метку с текстом «Авторизация», под ней 2 текстовых
поля и метки слева от них («Логин:», «Пароль:»), а уже под этими элементами выведите кнопку («Войти»).
Примечание: разумеется, форма должна выглядеть аккуратно, всё должно быть выравнено.
"""
from mod_set_win import *


o = window_setting()
l_1 = Label(o, text="Authorize")
l_2 = Label(o, text="Login")
l_3 = Label(o, text="Password")
t_l = Text(o, width=15, height=1)
t_p = Text(o,width=15, height=1)
b_1 = Button(o, text="Enter")

l_1.place(relx=0.5, rely=0.35)
l_2.place(relx=0.47, rely=0.4)
l_3.place(relx=0.47, rely=0.45)
t_l.place(relx=0.54, rely=0.4)
t_p.place(relx=0.54, rely=0.45)
b_1.place(relx=0.5, rely=0.5)

o.mainloop()