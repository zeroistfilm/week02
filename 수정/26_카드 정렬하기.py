# [백준] https://www.acmicpc.net/problem/1715 카드 정렬하기

import sys
import heapq
# sys.stdin = open('text/26.txt')


heap = []
heapq.heapify(heap)

N = int(sys.stdin.readline().strip())
sum = 0
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    heapq.heappush(heap, num)

if N == 1:
    print(0)
    exit(0)
elif N == 2:
    sum = heapq.heappop(heap) + heapq.heappop(heap)
else:
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        sum = sum + a+b
        heapq.heappush(heap, a+b)
print(sum)
