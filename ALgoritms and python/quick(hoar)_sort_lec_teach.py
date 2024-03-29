# -*- coding: utf-8 -*-
"""quick(hoar)_sort_lec_teach.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T575KXBsvlWelpIGIOvo0Nq_KKu3ud01
"""

def quick_sort(A:list) -> None: #Toni Hoara, доп память О(n)
    """ быстрая сортировка Тони Хоара
        сортирует список А
    """
    N = len(A)
    if N <= 1:
        return
    barrier = A[0] # need random
    L, R, M = [], [], []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else: # x > barrier
            R.append(x)
    quick_sort(L)
    quick_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k+=1


def main():
    A = [1,2,3,7,4,2,9,10,4,1]
    quick_sort(A)
    print(A)


if __name__ == "__main__":
    main()