# https://www.acmicpc.net/problem/8983
# 나의 생각,,,
# x축에서 가장 가까운 사대 2개 찾기
# 애초에 y축 사거리가 넘어가는 동물은 못잡는다고 체크, 리스트에서 입력시 제거한다.
# 첫번째 동물을 기준으로 가까운 사대 2개를 찾아서 사거리 안에 들어오는 모든 동물을 잡았다고 체크,
# (못잡은 동물중 가장 가까운 사대 2개를 찾아서 사거리 안에 들어오는 모든 동물을 잡았다고 체크) * 반복
#
#======= 승현이의 도움을 받은 솔루션
# 동물이 입력이 되면 리스트에 담을 필요 없이 바로 비교한다.
# 입력된 x좌표에서 가까운 사대 2개를 찾아서 잡을 수 있으면 카운팅, 못잡으면 넘긴다.

from bisect import  bisect_left
import sys
M,N,L = map(int,sys.stdin.readline().split())
Mposition = sorted(list(map(int,sys.stdin.readline().split())))
#[1,4,6,9]
count=0


for i in range(N):
    x,y = map(int,sys.stdin.readline().split())


    left=0
    right=len(Mposition)-1
    while left<=right:
        mid=(left+right)//2
        if Mposition[mid]<=x:
            # 마지막 사대거나, 사대의 위치가
            if len(Mposition)-1 == mid or Mposition[mid+1]>x:
                break
            left=mid+1
        else:
            right=mid-1

    if abs(x-Mposition[mid])+y<=L:
        count+=1
    elif len(Mposition)>mid+1 and abs(x-Mposition[mid+1])+y <=L:
        count+=1

print(count)


# 2차풀이 왜 안되는지 모르겟음;
# from bisect import  bisect_left
# import sys
# M,N,L = map(int,sys.stdin.readline().split())
# Mposition = sorted(list(map(int,sys.stdin.readline().split())))
# #[1,4,6,9]
# count=0
#
#
# for i in range(N):
#     x,y = map(int,sys.stdin.readline().split())
#
#     nearstation=bisect_left(Mposition,x)
#
#     if nearstation ==0: #제일 왼쪽 사대일 경우 가까운 사대는 교
#         #1번과 2번
#         station1=0 #인덱스
#         station2=1
#     elif nearstation == len(Mposition)-1:
#         #마지막 이 선택되면 제일 가까운 사대는 마지막과 마지막 직전
#         station1 = len(Mposition) - 2
#         station2 = len(Mposition) - 1
#
#     else:
#         #그렇지 않다면 좌우 사대 거리 비교
#         distance1 = nearstation+1
#         distance2 = nearstation-1
#         if Mposition[distance1]-x > Mposition[distance2]-x:
#             station1 = nearstation
#             station2 = distance2 #가까운 위치로 선택
#
#     if L >= abs(Mposition[station1] - x) + y:
#         count += 1
#
#     elif L >= abs(Mposition[station2] - x) + y:
#         count += 1
#
#
# print(count)













#==================1차 풀이 시간 초과 ==================
#알고리즘에서 1초는 10의 8승이다.
#주어진 입력은 (1 ≤ M ≤ 100,000), L (1 ≤ L ≤ 1,000,000,000)이기 때문에 불가능하다  10^5*10^9 = 10^14  ㅎㅎ
#
# from bisect import bisect_left, bisect_right
#
# M,N,L = map(int,input().split())
# Mposition = list(map(int,input().split()))
#
# #M 사대수, Mposition 사대 위치
# #N 동물수
# #L 사거리
# animals=[]
# for i in range(N):
#     animals.append(list(map(int,input().split())))
# # [[7, 2], [3, 3], [4, 5], [5, 1], [2, 2], [1, 4], [8, 4], [9, 4]]
#
# # #2. 이분탐색을 위한 정렬
# animals.sort()
# # [[1, 4], [2, 2], [3, 3], [4, 5], [5, 1], [7, 2], [8, 4], [9, 4]]
# #
# animalsX=[]
# for i in range(len(animals)):
#     animalsX.append(animals[i][0])
#
# hunt=[False for i in range(N)]
# huntingcount=0
# for i in range(M): #사대를 돌아가며 체크하고
#     #일단 이중포문 에바고,,, 사거리가 넘지 않는 범위만 탐색하는 방안?
#     #이게 가능하려면 인덱싱을 해야하는데,,,,,,,,,,,,
#     #동물의 위치가 정렬되어 있으므로
#     #|| ----사거리---사대포지션----사거리---- ||가능 범위
#     # 2-------4-------6---------4-------10
#     #|| L+사대위치+L
#     #bisect_left 사용해보기
#     # 리스트에서 X를 삽입할 가장 작은 인덱스를 찾는 메서드
#     #bisect_right
#     # 리스트(동물리스트)에서 우측최대사거리가 들어갈 가장 오른쪾 인덱스
#     leftindex = bisect_left(animalsX,Mposition[i]-L)
#     rightindex = bisect_right(animalsX,Mposition[i]+L)
#
#     for j in range(leftindex,rightindex): # 동물을 돌아가며 체크하는데
#         if hunt[j]==False:#잡지못했거나 시도하지 못했다면 시도!\
#
#             #시간 초과가 나므로 사냥가능거리에 이진탐색 도입 시도
#             #범위를 초과하는 이상은 탐색하지 않는다.
#             # left=0
#             # right=len(animals)-1 #리스트의 인덱스
#             #
#             # while left<=right:
#             #     mid = (left+right)//2
#
#                 # animals[mid] 중간값 추출
#                 # 추출한 값으로 거리 산출을 해야하는데................
#
#             if L>=abs(Mposition[i]-animals[j][0])+animals[j][1]:
#                 #사정거리 안에 들어온다면
#                 hunt[j]=True
#                 huntingcount+=1
#
# print(huntingcount)