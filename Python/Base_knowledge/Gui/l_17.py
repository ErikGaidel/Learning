"""
1) Выведите, используя метку, в окне такую строку: «ax^2 + bx + c = 0».
2) Добавьте 3 текстовых поля с метками «a:», «b:» и «c:».
3) Добавьте кнопку «Вычислить корни уравнения».
4) После вычисления их нужно вывести под кнопкой в формате: «x1 = …; x2 = …;».
5) Если число под корнем отрицательное, то вывести в метке для результата строку: «Нет корней».
Примечание:
"""
from mod_set_win import *
global t_1
global t_2
global t_3
global ans


def click(event=False):
    if event:
        print(event)
    try:
        d = float(t_2.get())**2 - 4 * float(t_1.get()) * float(t_3.get())
        if d < 0:
            ans.config(text="No solutions")
        elif d == 0:
            x_1 = str((-1) * float(t_2.get()) / (2 * float(t_1.get())))
            ans.config(text="x_1 = " + x_1 )
        else:
            x_1 = str(((-1)*float(t_2.get()) + d**0.5) / (2 * float(t_1.get())))
            x_2 = str(((-1)*float(t_2.get()) - d**0.5) / (2 * float(t_1.get())))
            ans.config(text="x_1 = " + x_1 + "; x_2 = " + x_2)
    except ValueError:
        ans.config(text="Bad request")


o = window_setting(w=1000)
l_0 = Label(o, text="Program to solve quadratic equation like ax^2 + bx + c = 0", font="Tahoma 20")
t_1 = Entry(o, font="Tahoma 20")
l_1 = Label(o, text="Enter a: ", font="Tahoma 20")
t_2 = Entry(o, font="Tahoma 20")
l_2 = Label(o, text="Enter b: ", font="Tahoma 20")
t_3 = Entry(o, font="Tahoma 20")
l_3 = Label(o, text="Enter c: ", font="Tahoma 20")
ans = Label(o, font="Tahoma 20")


b_1 = Button(o, text="Solve the equation", font="Tahoma 20", command=click)


l_0.grid(row=0, column=0, columnspan=2, ipadx=100, sticky="ne")
t_1.grid(row=1, column=1, sticky="w")
l_1.grid(row=1, column=0, sticky="e")
t_2.grid(row=2, column=1, sticky="w")
l_2.grid(row=2, column=0, sticky="e")
t_3.grid(row=3, column=1, sticky="w")
l_3.grid(row=3, column=0, sticky="e")
b_1.grid(row=4, column=0, pady=20, columnspan=2, sticky="s")
ans.grid(row=5, column=0, columnspan=2, sticky="s")
o.mainloop()
