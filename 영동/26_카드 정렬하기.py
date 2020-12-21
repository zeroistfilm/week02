# https://www.acmicpc.net/problem/1715

import heapq

N = int(input())
heap=[]
for i in range(N):
    heapq.heappush(heap,int(input()))

result=0
while len(heap)!=1:

    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum = one+two
    result+=sum
    heapq.heappush(heap,sum)

print(result)
