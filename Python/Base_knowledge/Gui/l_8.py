"""
1) Добавьте scrollbar к текстовой области из упражнения к уроку «Текстовая область».
Примечание: при необходимости в текстовый файл надо добавить ещё текста, чтобы scrollbar стал активным.
"""
from mod_set_win import *

file = open("file.txt", "w")
file.write("ngfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.close()

file = open("file.txt", "a")
file.write("1gfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.write("2gfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.write("3gfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.write("4gfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.write("5gfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.write("6gfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.write("7gfhnsdavhqaovhoaioigiwgwjxgjwgjoqiwrjgiqjeorgjoqijgqoqirjgiqjrogqhroqrgpqrgjqorigjqjrgqjrogjqrgjqorhnvgah")
file.close()

o = window_setting()
text = Text(o, width=30, height=10, font="Tahoma 30", bd=3)
scroll = Scrollbar(o, command=text.yview, orient=VERTICAL)
text["yscrollcommand"] = scroll.set
file = open("file.txt")
buf = file.read()
file.close()

text.insert(END, buf)
text.pack(side="left")
scroll.pack(side="left", fill=Y)
o.mainloop()
