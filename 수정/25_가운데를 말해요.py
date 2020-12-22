# [백준] https://www.acmicpc.net/problem/1655 가운데를 말해요
# [참고] https://peisea0830.tistory.com/59

import sys
import heapq

sys.stdin = open('text/25.txt')
N = int(sys.stdin.readline().strip())

numbers = []
maxheap = []
minheap = []
i = 0
for line in sys.stdin:
    i += 1
    numbers.append(int(line.strip()))

# # 0
# print(numbers[0])
# heapq.heappush(maxheap, [-numbers[0], numbers[0]])
#
# # 1
# print(numbers[0]) if numbers[0] < numbers[1] else print(numbers[1])
# heapq.heappush(minheap, numbers[1])

# 2
for i in range(0,N-1, +2):
    if numbers[i] > numbers[i+1]:       # 짝수면 maxheap
        heapq.heappush(maxheap, [-numbers[i], numbers[i]])
    else:                               # 홀수면 minheap
        heapq.heappush(minheap, numbers[i])
    a = minheap[-1] if minheap[-1] < maxheap[0][1] else maxheap[0][1]
    print(a)
    if numbers[i] > numbers[i+1]:       # 짝수면 maxheap
        heapq.heappush(minheap, numbers[i+1])
    else:                               # 홀수면 minheap
        heapq.heappush(maxheap, [-numbers[i+1], numbers[i+1]])
    a = minheap[-1] if minheap[-1] < maxheap[0][1] else maxheap[0][1]
    print(a)
    # max = maxheap[0][1]
    # min = minheap[0]
    # if max < min:
    #     heapq.heappush(maxheap, [-min, min])
    #     heapq.heappush(minheap, max)
    # else:

    # a =  N//2 +1 if N % 2 != 0 else N//2

# 중앙값의 특성: 그 값을 기준으로 작은 원소그룹, 큰 원소그룹을 나눴을 때,
# 작은그룹에서는 가장 큰 값이고 큰 그룹에서는 가장 작은 값이다.
