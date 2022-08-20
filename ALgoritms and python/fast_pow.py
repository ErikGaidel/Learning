# -*- coding: utf-8 -*-
"""fast_pow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1orpPuTlNcSPD7yEy05jOzAAlivi0ggH5
"""

def f_pow(a:float,n:int): # O(log2n)
    assert n >= 0
    assert a > 0
    if n == 0:
        return 1
    elif n % 2 == 1:
        return f_pow(a,n-1) * a
    else: # n % 2 == 0
        return f_pow(a**2, n // 2)

