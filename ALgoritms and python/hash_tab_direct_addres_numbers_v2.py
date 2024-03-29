# -*- coding: utf-8 -*-
"""hash_tab_direct_addres_numbers_v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lrd9-K0TMNChXEQgS6NJQqARNANWjjro
"""

class PhoneBook:
    def __init__(self):
        self.phones = dict()
        
    def find(self, phone_number):
        if phone_number not in self.phones:
            print('not found')
            return
        print(self.phones[phone_number])
    
    def add(self, phone_number, phone_holder):
        self.phones[phone_number] = phone_holder
        
    def _del(self, phone_number):
        if phone_number in self.phones:
            del self.phones[phone_number]

n = int(input())
pb = PhoneBook()
funcs = {'find': lambda phone: pb.find(phone),
         'add': lambda phone, name: pb.add(phone, name),
         'del': lambda phone: pb._del(phone)}
for _ in range(n):
    f, *args = input().split()
    funcs[f](*args)