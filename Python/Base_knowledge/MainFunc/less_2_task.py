"""
1) Попросите пользователя ввести произвольную строку.
2) Выведите коды всех символов строки, введённой пользователем.
3) Попросите пользователя ввести строку, состоящую только из цифр.
4) Используя соответствующую функцию, проверьте введённую пользователем строку, и если он ввёл правильно, то написать
«Спасибо!», иначе выбросить исключение, в обработке которого вывести строку «Некорректный ввод!».
"""

str_1 = input("Enter some string: ")
print("Your string is:", str_1)
str_2 = "ord({letter}) = {ord}"
for i in str_1:
    print(str_2.format(letter=i, ord=ord(i)))

# if u need codes of letters without reiterations
arr = set(str_1)
print(arr)
for i in arr:
    print(str_2.format(letter=i, ord=ord(i)))

str_3 = input("Enter some string consist only from digit's: ")
print("Your string is:", str_3)
try:
    if not str_3.isdigit():
        raise Exception("Incorrect enter!")
    print("Thanks for correct enter!")
except Exception as exp:
    print(exp)
