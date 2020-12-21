# [백준] acmicpc.net/problem/2164 카드2
import sys

N = int(sys.stdin.readline().strip())

tmp =[]
front = 1
rear = N - 1

num = N #일단 N개까지 감

if N == 1 or N == 2:
    print(N)
else:
    for i in range(N+1):
        tmp.append(i)
    while True:
        # for i in range(front, num,+2):   #일단 짝수만 담음
            # if i != rear+1:       #i가 마지막이 아니면
        # 현재 tmp 기준 인덱스가 홀수면 버리고 짝수면 담는다.
        for i in range(front, num):
            if i%2 == 0:
                tmp.append(tmp[i])
        num = len(tmp)
        front = rear +1
        rear = num - 1
        if front == rear:
            print(tmp[front])
            break
