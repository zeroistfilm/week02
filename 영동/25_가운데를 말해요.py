# https://www.acmicpc.net/problem/1655
# 내풀이 주어진 배열을 복사, 삭제하는 과정은 효율적이지 않다
import heapq
import sys
N = int(sys.stdin.readline())

minheap = []
j=0
for i in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(minheap, x)
    tmp=minheap[:]
    for k in range(j):
       heapq.heappop(tmp)
    print(heapq.heappop(tmp))
    if len(minheap)%2==0:
        j+=1
