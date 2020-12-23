# [백준] https://www.acmicpc.net/problem/1655 가운데를 말해요
# [참고] https://peisea0830.tistory.com/59
# [참고2] https://regularmember.tistory.com/142

import sys
import heapq

# sys.stdin = open('text/25.txt')
N = int(sys.stdin.readline().strip())

numbers = []
maxheap = []
minheap = []
heapq.heapify(maxheap)
heapq.heapify(minheap)
# 중앙값의 특성: 그 값을 기준으로 작은 원소그룹, 큰 원소그룹을 나눴을 때,
# 작은그룹에서는 가장 큰 값이고 큰 그룹에서는 가장 작은 값이다.

# ※ 만약 maxheap의 길이가 minheap과 같다면 maxheap에 원소를 넣고, 아니라면 minheap에 원소를 넣는다.
# ※ 만약 maxheap의 top이 minheap의 top보다 크다면 두 원소의 자리를 바꾼다.

for i in range(N):
    num = int(sys.stdin.readline().strip())
    if len(maxheap) == len(minheap):
        heapq.heappush(maxheap, (-num, num))

    else:
        heapq.heappush(minheap, num)

    if len(maxheap) != 0 and len(minheap) != 0 and maxheap[0][1] > minheap[0]:
        a = heapq.heappop(maxheap)
        b = heapq.heappop(minheap)
        a = a[1]
        b = (-b, b)

        heapq.heappush(maxheap, b)
        heapq.heappush(minheap, a)

    print(maxheap[0][1])
