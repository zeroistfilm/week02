# https://www.acmicpc.net/problem/2164
from collections import deque


N = int(input())
queue=deque()
for i in range(1,N+1):
    queue.append(i)


while len(queue)!=1: #1이 아닐때 반복
    if len(queue)==1:
        break
    else:
        queue.popleft()
        queue.append(queue.popleft())

print(queue[0])