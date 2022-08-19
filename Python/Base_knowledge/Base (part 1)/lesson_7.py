print("Введите 0, 1 или 2:")
a = input()
if a == "0":
    print(" U enter 0")
    print("this number less than 10")
    if 5 == 5:
        print("obviously")
elif a == "1":
    print(" U enter 1")
elif a == "2":
    print(" U enter 2")
else:
    print("Bad input")

cond = a == "0" or a == "1" or a == "2"

if cond:
    x = 0
else:
    x = 3
print("x= ", x)

x = 0 if cond else 3
print("x=", x)

#  task 7
n_1 = int(input("Enter first number:"))
n_2 = int(input("Enter second number:"))
if n_2 != 0:
    ans = n_1/n_2
else:
    ans = "infinity"
print(n_1, "/", n_2, "=", ans)