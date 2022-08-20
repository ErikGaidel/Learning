# -*- coding: utf-8 -*-
"""lec_bin_search.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NgULCBq2dDV4baKUbzTACNSPYo55GrLe
"""

def left_bound(A:list, key:int) -> int:
    """ funcion to search max num left that left < key"""
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left+right)//2
        if A[mid] < key:
            left = mid
        else:
            right = mid
    return left


def right_bound(A:list, key:int) -> int:
    """ funcion to search min num right that right > key """
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left+right)//2
        if A[mid] <= key:
            left = mid
        else:
            right = mid
    return right


def bin_search(A:list, key:int, first:bool = True) -> int:
    """ funcion to search key and return
        if first the first meeting in list
        if not first the last meeting in list
        if not in list return -1
    """
    right = right_bound(A,key)
    left = left_bound(A,key)
    if right - left > 1:
        if first:
            return left + 1
        return right - 1
    return -1


def test():
    assert bin_search([-2,-1,-1,0,1,1,1,2,3,3,5,5,5,6,8,9], 5) == 10
    assert bin_search([-2,-1,-1,0,1,1,1,2,3,3,5,5,5,6,8,9], 5, False) == 12
    assert bin_search([-2,-1,-1,0,1,1,1,2,3,3,5,5,6,8,9], 10) == -1
    assert bin_search([], 5) == -1
    assert bin_search([-2,-1,-1,0,1,1,1,2,3,3,5,5,6,8,9], -1) == 1
    assert bin_search([-2,-1,-1,0,1,1,1,2,3,3,5,5,6,8,9], 0) == 3


if __name__ == "__main__":
    test()