# https://www.acmicpc.net/problem/1655
# 내풀이 주어진 배열을 복사, 삭제하는 과정은 효율적이지 않
# import heapq
# import sys
# N = int(sys.stdin.readline())
#
# minheap = []
# j=0
# for i in range(N):
#     x = int(sys.stdin.readline())
#     heapq.heappush(minheap, x)
#     tmp=minheap[:]
#     for k in range(j):
#        heapq.heappop(tmp)
#     print(heapq.heappop(tmp))
#     if len(minheap)%2==0:
#         j+=1

#====================
import heapq
import sys
N = int(sys.stdin.readline())
minheap=[]
maxheap=[]

for i in range(N):
    x = int(sys.stdin.readline().strip())

    if i%2!=0: #짝수번째로 들어오는것

        heapq.heappush(minheap, (x,x))
    else:

        heapq.heappush(maxheap,(-x,x))

    if i==0:
        print(maxheap[0][1])
    else:
        if minheap[0][1] > maxheap[0][1]:
            print(maxheap[0][1])
        else:
            maxhh= heapq.heappop(maxheap)
            minhh= heapq.heappop(minheap)
            heapq.heappush(minheap,(maxhh[1],maxhh[1]))
            heapq.heappush(maxheap, (-minhh[1],minhh[1]))

            print(maxheap[0][1])




