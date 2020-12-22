# [백준] https://www.acmicpc.net/problem/3190 뱀
# 뱀의 경로 구현에 덱 deque 자료구조를 이용해 시뮬레이션
from collections import deque
import sys
sys.stdin = open('text/23.txt')

def put():
    for i in range(N):
        print(board[i], end=' ')
        print()
    print()

N = int(input().strip())
board = []
for i in range(N):
    board.append(['□']*N)

K = int(input().strip())
for k in range(K):
    tmp = list(map(int, sys.stdin.readline().split()))
    board[tmp[0]-1][tmp[1]-1] = '★'
board[0][0] = '■'

turn = []
L = int(input().strip())
for l in range(L):
    turn.append(list(sys.stdin.readline().split()))

xturn = [1, 0, -1, 0]
yturn = [0, 1, 0, -1]
# 0 = 오른쪽 1 = 아래로 2 = 왼쪽 3 = 위로
sec = 0
snake = deque()
snake.append([0,0])
x = 0
y = 0
flag = 0
t = 0

xmove: int = xturn[t]
ymove: int = yturn[t]

while True:
     x += xmove
     y += ymove
     if x >= N or y >= N or x < 0 or y < 0:
         print(sec+1)
         break
     for i in snake:
         if i[0] == y and i[1] == x:
             print(sec+1)
             exit(0)

     snake.append([y, x])
     sec += 1
     if board[y][x] == '★':
        board[y][x] = '■'
     else:
        board[snake[0][0]][snake[0][1]] = '□'
        snake.popleft()
     board[y][x] = '■'
     # put()

     if len(turn) > 0 and str(sec) in turn[0]:


         if turn[0][1] == 'D':
             t += 1
             if t == 4: t = 0

         else:
             t -= 1
             if t == -1 : t = 3

         xmove = xturn[t]
         ymove = yturn[t]
         del turn[0]


