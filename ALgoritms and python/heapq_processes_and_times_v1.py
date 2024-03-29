# -*- coding: utf-8 -*-
"""heapq_processes_and_times_v1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RkyLPr4uWUybZhWdIfPr0uHmJmTi_GPB
"""

import  heapq

n,m = map(int,input().split())
times = list(map(int,input().split()))

que = [[0,i] for i in range(n)]
heapq.heapify(que)
for i, t in enumerate(times):
    prev = heapq.heappop(que)
    print(*prev[::-1])
    prev[0] += t
    heapq.heappush(que,prev)