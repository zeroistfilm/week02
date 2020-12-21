# https://www.acmicpc.net/problem/11866
from collections import deque


N,K = map(int,input().split())
queue=deque()
for i in range(1,N+1):
    queue.append(i)
print('<',end="")
while len(queue)!=0:
    for _ in range(K-1):
        queue.append(queue.popleft())
    extracted=queue.popleft()
    if len(queue)==0:
        print(extracted, end="")
    else:
        print(extracted, end=", ")
print('>',end="")