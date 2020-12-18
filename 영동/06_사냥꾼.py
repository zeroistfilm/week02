# https://www.acmicpc.net/problem/8983
from bisect import bisect_left, bisect_right

M,N,L = map(int,input().split())
Mposition = list(map(int,input().split()))

#M 사대수, Mposition 사대 위치
#N 동물수
#L 사거리
animals=[]
for i in range(N):
    animals.append(list(map(int,input().split())))
# [[7, 2], [3, 3], [4, 5], [5, 1], [2, 2], [1, 4], [8, 4], [9, 4]]

# #2. 이분탐색을 위한 정렬
animals.sort()
# [[1, 4], [2, 2], [3, 3], [4, 5], [5, 1], [7, 2], [8, 4], [9, 4]]
#
animalsX=[]
for i in range(len(animals)):
    animalsX.append(animals[i][0])

hunt=[False for i in range(N)]
huntingcount=0
for i in range(M): #사대를 돌아가며 체크하고
    #일단 이중포문 에바고,,, 사거리가 넘지 않는 범위만 탐색하는 방안?
    #이게 가능하려면 인덱싱을 해야하는데,,,,,,,,,,,,
    #동물의 위치가 정렬되어 있으므로
    #|| ----사거리---사대포지션----사거리---- ||가능 범위
    # 2-------4-------6---------4-------10
    #|| L+사대위치+L
    #bisect_left 사용해보기
    # 리스트에서 X를 삽입할 가장 작은 인덱스를 찾는 메서드
    #bisect_right
    # 리스트(동물리스트)에서 우측최대사거리가 들어갈 가장 오른쪾 인덱스
    leftindex = bisect_left(animalsX,Mposition[i]-L)
    rightindex = bisect_right(animalsX,Mposition[i]+L)

    for j in range(leftindex,rightindex): # 동물을 돌아가며 체크하는데
        if hunt[j]==False:#잡지못했거나 시도하지 못했다면 시도!\

            #시간 초과가 나므로 사냥가능거리에 이진탐색 도입 시도
            #범위를 초과하는 이상은 탐색하지 않는다.
            # left=0
            # right=len(animals)-1 #리스트의 인덱스
            #
            # while left<=right:
            #     mid = (left+right)//2

                # animals[mid] 중간값 추출
                # 추출한 값으로 거리 산출을 해야하는데................

            if L>=abs(Mposition[i]-animals[j][0])+animals[j][1]:
                #사정거리 안에 들어온다면
                hunt[j]=True
                huntingcount+=1

print(huntingcount)