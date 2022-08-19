# task_12

str_1 = input("Enter some string:")
cort = (str_1,)
print(cort)
cort = tuple(str_1)
print(cort)
for i in cort:
    print(i, end=" ")
