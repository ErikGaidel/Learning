"""
1) Попросите пользователя указать, какое количество элементов надо создать в списке.
2) Сделайте цикл на соответствующее число итераций, в каждой из которых просите пользователя ввести число в таком
формате: «Введите число N:», где N – текущий номер числа.
3) Добавляйте каждое это число в список.
4) По завершению цикла выведите получившийся список.
"""
while True:
    n = input("Enter size of list: ")
    if n.isdigit():
        n = int(n)
        break
    elif n == "exit":
        exit(0)
    else:
        print("U need enter a digit or write 'exit'!")
        continue

str_1 = "Enter the {num} number "
lis = []

for i in range(0, n):
    while True:
        num = input(str_1.format(num=i + 1))
        if num.isdigit() :
            break
        elif num == "exit":
            exit(0)
        else:
            print("U need enter a digit or write 'exit'!")
            continue
    lis.append(num)

print("Yours list is: ", lis)
