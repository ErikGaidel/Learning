#  task_14

def parity(x):
    if x % 2 == 0:
        return True
    else:
        return False


def max_el(arr):
    maxes = arr[0]
    for n in arr:
        if n > maxes:
            maxes = n
    return maxes


def average(*numbers):
    s = 0
    i = 0
    for n in numbers:
        s += n
        i += 1
    return s/i


print(parity(11))
print(max_el([3, 52, 21, 532, 7, 537]))
print(average(10, 20, 30, 40, 50))
