"""
1) Создайте словарь из 3-х ключей «Hello», «Bуe» и «Lesson» и значениями соответственно «Здравствуй», «Пока» и «Урок».
2) В бесконечном цикле выводите случайное значение из словаря и просите пользователя написать перевод на английском.
3) Проверяйте на соответствие введённой пользователем строки и ключа словаря. Если пользователь ввёл всё правильно,
то выводить ему следующее слово. Если неправильно, то сообщать ему об этом, и заново ждать от него уже другого ответа.
 И так до тех пор, пока он не введёт правильный ответ.
4) Если пользователь вводит команду «show», то вывести словарь.
5) Если пользователь вводит «quit», то завершать программу.
Примечание: не забывайте, что если пользователь будет писать, например: «hello», «Hello» или «HELlo» - то это всё
считать правильными ответами.
"""
import random

d = dict(Hello='Привет', Bye='Пока', Lesson="Урок")
print("Welcome to teaching English! Enter 'show' to see dictionary of words, or enter 'quit' to exit from programme")
check = list(d.keys())
while True:
    c = random.random()*3
    if c < 1:
        print("Translate in English: ", d["Hello"])
        c = 0
    elif c < 2:
        print("Translate in English: ", d["Bye"])
        c = 1
    else:
        print("Translate in English: ", d["Lesson"])
        c = 2
    while True:
        val = input("Enter translate  word higher in English: ")
        if val.lower() == "quit":
            exit(0)
        elif val.lower() == "show":
            print(d)
        elif val.lower() == check[c].lower():
            print("Alright!")
            break
        else:
            print("Incorrect!")
            continue
