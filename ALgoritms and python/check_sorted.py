# -*- coding: utf-8 -*-
"""check_sorted.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T575KXBsvlWelpIGIOvo0Nq_KKu3ud01
"""

def check_sorted(A:list, asc = True) -> bool: 
    """ проверка отсортированости за О(N)
    """
    for i in range(len(A)-1):
        if ( (A[i] > A[i+1]) if asc else (A[i]<A[i+1]) ):
            return False
    return True


def main():
    A = [1,2,3,7,4,2,9,10,4,1]
    B = [1,2,3,4,4,5,6,7,7,8]
    C = [8,7,7,6,5,4,4,3,2,1]
    print(check_sorted(A))
    print(check_sorted(B))
    print(check_sorted(C,False))
    #print(A)


if __name__ == "__main__":
    main()