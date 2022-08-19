# -*- coding: utf-8 -*-
"""heapq_processes_and_times_v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RkyLPr4uWUybZhWdIfPr0uHmJmTi_GPB
"""

n, m = map(int, input().split(' '))
tasks = list(map(int, input().split(' ')))
p = [i for i in range(n)] #процессоры, приоритет = время работы * n + номер процессора
for i in range(m):
    #в корне свободный процессор с минимальным номером
    print(p[0] % n, p[0] // n)
    p[0] += tasks[i] * n
    #топим корень
    j, l, r = 0, 1, 2
    while l < n and p[j] > p[l] or r < n and p[j] > p[r]:
        if r >= n or p[j] > p[l] and p[r] > p[l]:
            p[j], p[l] = p[l], p[j]
            j = l
        else:
            p[j], p[r] = p[r], p[j]
            j = r
        l = j * 2 + 1
        r = l + 1