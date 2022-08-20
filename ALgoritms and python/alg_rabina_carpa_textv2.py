# -*- coding: utf-8 -*-
"""alg_rabina_carpa_textv2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1op6GMW_K_OhIaLBxg1YLeBeG1OuSocRv
"""

#исходные строки, сразу переводим коды, с учетом ord('A') == 65
pattern = [ord(s) - 65 for s in input()]
text = [ord(s) - 65 for s in input()]
#константы
m, n = len(pattern), len(text)
x, p = 59, 67 # простые
#степени x от 1 до m-1 по модулю p (чтобы не пересчитывать)
x_pows = [1]
for i in range(1, m):
    x_pows.append(x_pows[-1] * x % p)
#хеш паттерна в обратную сторону (тогда вывод идет в прямом порядке):
#pattern[0] * x ^ (m-1)  + pattern[1] * x ^ (m-2) + ... pattern[m-1]
pattern_hash = sum([pattern[i] * x_pows[m-i-1] for i in range(m)]) % p
#последние мономы в хеше: text[i] * x ^ (m-1)
last_monoms = [text[i] * x_pows[-1] % p for i in range(n - m + 1)]
#хеш первой подстроки, тоже в обратную сторону
cur_hash = (last_monoms[0] + sum([text[i] * x_pows[m-i-1] for i in range(1, m)])) % p
#цикл в прямом порядке
for i in range(n - m):
    #проверяем совпадение хеша и подстроки
    if pattern_hash == cur_hash and pattern == text[i:(i+m)]:
        print(i, end = ' ')
    #пересчет хеша (в начале выталкиваем макс. степень, в конце прибавляем 0-вую
    cur_hash = ((cur_hash - last_monoms[i]) * x + text[i + m]) % p
#последняя подстрока, если добавить в цикл, то в пересчете хеша выйдем за границы массива
if pattern_hash == cur_hash and pattern == text[(n-m):]:
    print(n - m, end = ' ')