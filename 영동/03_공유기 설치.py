# https://www.acmicpc.net/problem/2110

import sys
N,C = map(int,sys.stdin.readline().split())

house=[]
for i in range(N):
    house.append(int(sys.stdin.readline().strip()))

house.sort()

left=1 #가능한 최소 거리
right=house[-1]-house[0]
d=0
ans=0
start=house[0]
while left<=right:

    mid = (left+right)//2
    cnt=1


    #==============================================
    #일반적인 이진탐색에서 조건문이 추가된 구조이다.
    #
    for i in range(N):
        d = house[i]-start #간격 1, 2, 3, 4, 5 ....
        if mid<=d: # 현재 위치와 직전 설치한 공유기의 위치의 간격이 mid 보다 크다면
            cnt+=1
            start=house[i]

    #==============================================

    if cnt>=C:
        #공유기 수를 줄이자 => 간격 넓히기
        ans = mid
        left = mid+1
    else:
        #공유기 더 설치되어야함 간격 좁히기
        right = mid-1

print(ans)