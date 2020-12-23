# [백준] https://www.acmicpc.net/problem/13334 철로
import sys
import heapq
sys.stdin = open('text/27.txt')

N = int(input())
prique = []
heapq.heapify(prique)

for _ in range(N):
    mi, ma= list(map(int, sys.stdin.readline().split()))
    if mi > ma:
        mi, ma = ma, mi
    heapq.heappush(prique, (mi, ma))

D = int(sys.stdin.readline().strip())
i = 0

while len(prique) > i:
    if prique[i][1] - prique[i][0] > D:
        del prique[i]
    else:
        i += 1

cnt = 0
largest = 0

while prique:

    cnt = 1
    left = heapq.heappop(prique)[0]
    l = len(prique)
    for i in range(l):
        if left + D >= prique[i][1]:
            cnt += 1
    if cnt > largest:
        largest = cnt
print(largest)