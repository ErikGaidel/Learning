# -*- coding: utf-8 -*-
"""ways_to_get_N_with_steps.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xAx2FS5PVRKJ7UkvRV5_PgoJxPiij6pJ

0 1 1 2 3 5 8
"""

def count_ways_2st(n:int)->int:
    """ num of ways to get N by 2 kind of steps: +1 and + 2
        begin 1 step"""
    K = [0,1] + [0]*(n-1)
    for i in range(2,n+1):
        K[i] = K[i-2] + K[i-1]
    return K[n]


def count_ways_3st_with_allow(n:int, allowed:list = None)->int:
    """ num of ways to get N by 3 kind of steps: +1, + 2, +3
        and with some steps are not allowed ( if allowed[step] = 0)
        begin 1 step"""
    if not allowed:
        allowed = [1] * (n+1)
    K = [0,1,allowed[2]] + [0]*(n-2)
    for i in range(3,n+1):
        if allowed[i]:
            K[i] = K[i-1] +  K[i-2] + K[i-3]
    return K[n]


def count_way_2st_with_min_cost(n:int, price:list = None)->int:
    """ num of ways to get N by 2 kind of steps: +1 and + 2
        with min cost, price[i] - cost to get this step 
        by default calc the min num of steps to get step N"""
    if not price:
        price = [1] * (n+1)
    C = [float("inf"), price[1], price[1]+price[2]] + [0]*(n-2)
    for i in range(2,n+1):
        C[i] = price[i] + min(C[i-2],C[i-1])
    return C[n]


def best_way_2st_with_min_cost(n:int, price:list = None)->int:
    """ num of ways to get N by 2 kind of steps: +1 and + 2
        with min cost, price[i] - cost to get this step 
        by default calc the min num of steps to get step N
        return cost and best way"""
    if not price:
        price = [1] * (n+1)
    C = [(float("inf"),-1),(price[1],0), (price[1]+price[2],1)] + [0]*(n-2)
    for i in range(2,n+1):
        if C[i-1][0] < C[i-2][0]:
            C[i] = (price[i] + C[i-1][0], i-1)
        else:
            C[i] = (price[i] + C[i-2][0], i-2)
    way, prev = [n], C[n][1]
    while prev != -1:
        way.append(prev)
        prev = C[prev][1]
    return C[n][0], way


def test():
    print(count_ways_2st(5))
    print(count_ways_3st_with_allow(5))
    print(count_way_2st_with_min_cost(5))
    print(best_way_2st_with_min_cost(5))
    assert count_ways_2st(5) == 5


if __name__ == "__main__":
    test()