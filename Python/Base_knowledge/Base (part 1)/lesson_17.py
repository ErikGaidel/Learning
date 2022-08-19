#  print(10 / 0) деление на ноль генерирует исключение

try:
    a = float(input("Enter dividend: "))
    b = float(input("Enter divisor: "))
    print("Result", a/b)
except ZeroDivisionError:
    print("Infinity")
