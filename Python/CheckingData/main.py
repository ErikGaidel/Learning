# -*- coding: utf-8 -*-
"""
Есть файл с протоколом регистраций пользователей на сайте (registrations.txt).<br>
Каждая строка содержит информацию о имени, электронной почте и возрасте человека. <br><br>

Надо проверить данные из файла, для каждой строки:
 - присутсвуют все три поля
 - поле имени содержит только буквы
 - поле email содержит @ и .
 - поле возраст является числом от 10 до 99<br>

В результате проверки нужно сформировать два файла
 - registrations_good.log для правильных данных, записывать строки как есть
- registrations_bad.log для ошибочных, записывать строку и вид ошибки.<br>

Для валидации строки данных написать метод, который может выкидывать исключения:
 - НЕ присутсвуют все три поля: ValueError
 - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
 - поле email НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
 - поле возраст НЕ является числом от 10 до 99: ValueError
Вызов метода обернуть в try-except.
"""


class Valid:

    def checking(self, line, count):
        try:
            result = None
            name, email, age = line.split()
            if not name.isalpha():
                raise NotNameError(f"Поле имени содержит не только буквы в: {line}")
            if "@" not in email or "." not in email:
                raise NotEmailError(f"Поле email не содержить . или @ в: {line}")
            if not 10 <= int(age) <= 99:
                raise ValueError("Не от 10 до 99")
        except ValueError as exc:
            if exc.args[0] == "Не от 10 до 99":
                result = f"Поле возраст НЕ является числом от 10 до 99 в: {line}"
                count += 1
            else:
                result = f"{exc} in: {line}"
                count += 1
        except NotNameError as exc:
            result = f"{exc}"
            count += 1
        except NotEmailError as exc:
            result = f"{exc}"
            count += 1
        return count, result


class NotNameError(BaseException):

    def __int__(self, mess):
        self.message = mess


class NotEmailError(BaseException):

    def __int__(self, mess):
        self.message = mess


count_bad = 0
a = Valid()
with open("registrations_.txt", "r", encoding="UTF-8") as ff:
    for line in ff:
        try:
            count_bad, result = a.checking(line, count_bad)
            if result is None:
                with open ("registrations_good_log.txt", "a", encoding="UTF-8") as fg:
                    fg.write(line)
            else:
                with open ("registrations_bad_log.txt", "a", encoding="UTF-8") as fb:
                    fb.write(result)
        except:
            print (f"Something wrong, now we work with {line}")
            ff.close()
            fg.close()
            fb.close()

print(count_bad)
