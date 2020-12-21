# https://www.acmicpc.net/problem/1655
# 내풀이
import heapq
import sys
import copy
N = int(sys.stdin.readline())

minheap = []
j=0
for i in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(minheap, x)
    tmp=copy.deepcopy(minheap)
    for k in range(j):
       heapq.heappop(tmp)
    print(heapq.heappop(tmp))
    if len(minheap)%2==0:
        j+=1
