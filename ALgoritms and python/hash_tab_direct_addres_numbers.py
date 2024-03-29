# -*- coding: utf-8 -*-
"""hash_tab_direct_addres_numbers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lrd9-K0TMNChXEQgS6NJQqARNANWjjro
"""

T = ["" for i in range(10**7)]


def add_number(numb:int, name:str):
    T[numb] = name


def del_number(numb:int):
    if T[numb]:
        T[numb] = ""


def find_number(numb:int):
    if T[numb]:
        print(T[numb])
        return
    print("not found")


def treatment_req(req:str):
    req = req.split()
    if req[0] == "add":
        add_number(int(req[1]),req[2])
    elif req[0] == "del":
        del_number(int(req[1]))
    elif req[0] == "find":
        find_number(int(req[1]))


def main():
    n = int(input())
    for _ in range(n):
        request = input()
        treatment_req(request)


if __name__ == "__main__":
    main()