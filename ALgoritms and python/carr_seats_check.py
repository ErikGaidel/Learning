# -*- coding: utf-8 -*-
"""Carr_seats_check.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1buPn0h1aPjrMtt1XSEp9uWLPjBSoC51b
"""

import numpy as np
import math


def out_func(ans:np.ndarray):
    """
    функция вывода в файл ответа
    input:
    ans - массив с ответами о возможности восстановления
    return: None
    функция ничего не возращает
    """
    np.savetxt("output.txt", ans, fmt="%d", delimiter=" ")


def check_line_seats(line:list, lim:int):
    """
    
    """
    seat = 0
    for subl in line:
        L = min(lim,len(subl))
        IT = math.ceil(len(subl)/L)
        for it in range(IT):
            nfs = 0
            for s in range(it,L+it):
                if lim==2:
                    print(subl, subl[s], s, it)
                if subl[s] == "X":
                    if nfs == 0:
                        nfs += 1
                    else:
                        return -1
            if nfs == 0:
                seat += 1
    return seat


def check_vag_seats(vag_seq:list, k:int):
    """
    
    """
    seats = np.zeros(k)
    for line in vag_seq:
        if line.pop(0) == "#":
            seats = seats + ones
        for i in range(k):
            seat = check_line_seats(line, i+1)
            if seat == -1:
                for j in range(i,k):
                    seats[j] = -1
                break
            else:
                seats[i] += seat
    return seats


vagon_seq = [] # список для считывания рядов в вагонах
k = 6
ones = np.ones(k)

# считываем наши данные
with open("input.txt") as inp_file:
    n = int(inp_file.readline()) # количество вагонов на проверку
    for _ in range(n):
        line_seq = []
        line_seq.append(inp_file.readline().replace("\n","").split(".."))
        inp_file.readline()
        line_seq.append(inp_file.readline().replace("\n","").split(".."))
        vagon_seq.append(line_seq)

ans_seq = np.zeros((n,k))

for i in range(n):
    ans = check_vag_seats(vagon_seq[i], k)
    ans_seq[i] = ans

out_func(ans_seq)
