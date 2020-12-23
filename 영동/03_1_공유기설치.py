# https://www.acmicpc.net/problem/2110
import sys
N,C = map(int,input().split())
homes=[]
for _ in range(N):
    homes.append(int(input()))

homes.sort()

start = 1
end = homes[-1]-homes[0]
max=0

while start<=end:
    mid=(start+end)//2
    ss = homes[0]
    setdivice = 1
    for i in range(N):
        distance = homes[i]-ss
        if mid<=distance:
            setdivice+=1
            ss =homes[i]

    if setdivice<C:
        end=mid-1
    else:
        start=mid+1
        max = mid



print(max)


