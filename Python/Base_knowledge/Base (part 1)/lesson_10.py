#  task_10
array = list(range(5, 17, 2))
print("Our array is ", array)
s = 0
for i in array:
    s += i
print("Sum of numbers in array:", s)
sa = s/len(array)
print("Average of all numbers in array:", sa)
