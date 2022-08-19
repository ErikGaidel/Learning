#  task_9
list_str = ["asd", "asides", "rebounds", "aggro", "rugs", "asleep"]
i = 0
while i < len(list_str):
    print(i, "element is", list_str[i])
    i += 1

while True:
    n = input("Enter index of element u wanna see or exit to quit:")
    if n == "exit":
        break
    if int(n) > len(list_str)-1:
        print("Bad index")
        continue
    print("Your element is", list_str[int(n)])
