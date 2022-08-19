#  lesson_6

my_str1 = "abc"
my_str2 = "xyx"
print("конкатенация двух строк =", my_str1 + my_str2)

my_str3 = """ Long long string
for a few
strings"""
print(my_str3)
number1 = input("Input 1 number: ")
print("U are input:", number1)
print("Input 2 number:")
number2 = input()
print("U are input:", number2)
print("Сумма строк = ", number1+number2)

print("Сумма чисел = ", float(number1)+float(number2))
print("Сумма чисел = ", int(number1)+int(number2))

#  task_6
n1 = input(" Введите первое число:")
n2 = input(" Введите второе число:")
n3 = input(" Введите третье число:")
print("Среднее арифметическое введеных трех чисел = ", (int(n1)+int(n2)+int(n3))/3)
