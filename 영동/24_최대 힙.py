# https://www.acmicpc.net/problem/11279

import heapq
import sys

N = int(sys.stdin.readline())

heap=[]
for i in range(N):
    x = int(sys.stdin.readline())

    if x: #0이 아니면
        heapq.heappush(heap,(-x,x))
    else:
        if len(heap)>=1:
            print(heapq.heappop(heap)[1])
        else:
            print(0)


