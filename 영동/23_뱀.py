# https://www.acmicpc.net/problem/3190

from collections import deque
import copy

N = int(input())
K = int(input())
apples=[]
for _ in range(K):
    apples.append(list(map(int,input().split())))

L = int(input())
orders=deque()
for _ in range(L):
    orders.append(list(map(str,input().split())))

field = [[0 for i in range(1,N+1)]for j in range(1,N+1)]


direction = deque()
direction.append([0,1]) #우
direction.append([1,0]) #하
direction.append([0,-1])#좌
direction.append([-1,0])#상
for apple in apples:
    field[apple[0]-1][apple[1]-1]=1

snake = deque()
head = [0,0] #현재 위치임
snake.append(tuple(head))
field[head[0]][head[1]]=-1 #뱀이 있는 시작 위치
currentdirection= direction[0]# 시작 :현재 방향
#뱀 덱에는 좌표를 넣어줘야함
time=0 #1초에서 시작
while 0 < head[0] or head[0]<=N or 0 < head[0] or head[1]<=N:
    time += 1


    if len(orders)==0:
        pass
    else:
        if int(orders[0][0]) == time-1:
            if orders[0][1]=='D':
                direction.append(direction.popleft())
                currentdirection = direction[0]
            elif orders[0][1]=='L':
                direction.appendleft(direction.pop())
                currentdirection = direction[0]

            orders.popleft()
    #인덱스들
    #head  # 현재 위치[r,c]
    #direction[currentdirection] #방향 [r,c]
    # 현재 보는방향 앞칸의 위치의 필드값
    head[0] += currentdirection[0]
    head[1] += currentdirection[1]

    if 0 > head[0] or head[0] >= N or 0 > head[1] or head[1] >= N:
        break

    if field[int(head[0])][int(head[1])]==0:
        # print('앞에 갈 수 있음')
        snake.append(tuple(head))
        past=snake.popleft()
        for i in range(len(snake)): #뱀의 위치 업데이트 하면서 -1넣기
            field[snake[i][0]][snake[i][1]] = -1
        field[past[0]][past[1]]=0 #지나간자리 0으로 바꾸기


    elif field[int(head[0])][int(head[1])]==1:
        # print('앞에 사과가 있음')
        snake.append(tuple(head))
        for i in range(len(snake)): #뱀의 위치 업데이트 하면서 -1넣기
            field[snake[i][0]][snake[i][1]] = -1

    elif field[int(head[0])][int(head[1])]==-1:
        # print('몸에 부딪힘')
        break

print(time)




