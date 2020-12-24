import sys
import heapq
import copy

sys.stdin = open('03.txt')

K, N = sys.stdin.readline().split()
K = int(K)
N = int(N)
M = list(map(int, sys.stdin.readline().split()))
C = copy.deepcopy(M)
heapq.heapify(M)
heapq.heapify(C)


for j in range(N):
    result = heapq.heappop(C)
    for i in range(K):
        heapq.heappush(C, result*M[i])
        if result % M[i] == 0:
            break
print(result)
