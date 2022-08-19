# task_11
import random
n = input("Enter quantity of number's u need:")
array = [int(random.random() * 100) for i in range(0, int(n))]
i = 0
print("Array with duplicates:   ", end=" ")
while i < len(array):
    print(array[i], end=" ")
    i += 1

array = list(set(array))

print()
print("Array without duplicates:", end=" ")
i = 0
for i in array:
    print(i, end=" ")
