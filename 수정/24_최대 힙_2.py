# [백준] https://www.acmicpc.net/problem/11279 최대 힙
# heapq를 쓰자!
# [참고] https://duwjdtn11.tistory.com/555

import sys
import heapq

sys.stdin = open('text/24.txt')
N = int(sys.stdin.readline().strip())

heap =[]


for num in sys.stdin:
    num = int(num.strip())

    if num == 0:
        if heap:    # 힙에 원소가 있으면
            print(heapq.heappop(heap)[1])
        else:                   # 없으면
            print("0")

    else:
        heapq.heappush(heap, [-num, num])