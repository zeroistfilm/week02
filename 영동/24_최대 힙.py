# https://www.acmicpc.net/problem/11279

import heapq
import sys

N = int(sys.stdin.readline())

def minheapsort(array):
    result=[]
    heap=[]
    for i in array:
        heapq.heappush(heap,i)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

order =[]
for i in range(N):
    order.append(int(sys.stdin.readline()))

result=[]
for i in order:
    if i ==0:

        if len(result)==0:
            print(0)
        else:
            print(result.pop())

    else:
        result.append(i)
        result=minheapsort(result)


