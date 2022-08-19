#  task_8
#  bad solution of problem
"""
while True:
    s = 0
    n = 0
    while True:
        n = input("Enter number for recapitulation:")
        if n != "exit" and n != "sum":
            s += int(n)
            continue
        break
    if n == "exit":
        print("Exit from calculation's")
        break
    print("Sum of all entered numbers:", s)
"""

#  normal solution of problem
s = 0
n = 0
while True:
    n = input("Enter number for summation:")
    if n == "sum":
        print("Sum of all entered numbers:", s)
        s = 0
        continue
    elif n == "exit":
        print("Exit from calculation's")
        break
    else:
        s += int(n)
