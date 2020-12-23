# https://www.acmicpc.net/problem/13334

import heapq
import sys
N = int(input())

ls=[]
for i in range(N):
    tmp=list(map(int, sys.stdin.readline().split()))
    if tmp[0]>tmp[1]:
        tmp[0],tmp[1] = tmp[1],tmp[0]
    ls.append(tmp)
askdjaslkdjaslkjd
D = int(sys.stdin.readline())

ls.sort(key=lambda x:x[1])

pq=[]
max=0
for dis in ls:
    if dis[1]-D<=dis[0]:
        heapq.heappush(pq,dis) #철로 안에 시작점이 들어오면 큐에 넣는다
    while len(pq)!=0 and pq[0][0]<dis[1]-D: #철로 끝점이 집을 지나면 반복하며 지난 집을 뺀다.
        heapq.heappop(pq)

    if max<len(pq):
        max=len(pq)
print(max)
