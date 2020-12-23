# https://www.acmicpc.net/problem/1654

K,N = map(int,input().split())
import sys
lines=[]
for i in range(K):
    lines.append(int(input()))

lines.sort()

start = 1
end = lines[-1]#첫번째 값으로 설정
max=0
while  start <= end:
    count=0
    mid = (start+end)//2
    if mid ==0:
        break

    cutlength = mid
    for i in range(K): #라인수 만큼 반복
        count+=lines[i]//cutlength
    if count<N:
        end = mid - 1
    else:
        start = mid + 1
        if mid > max:
            max=mid
print(max)