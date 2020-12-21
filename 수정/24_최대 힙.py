# [백준] https://www.acmicpc.net/problem/11279 최대 힙
import sys
sys.stdin = open('text/24.txt')


def sort(idx):
    parent = idx // 2
    if len(que) == front + 1:  # 빈 배열이었음
        return
    elif parent < front:  # 빈 배열 아니었으므로 front에 값 있음
        parent = front

    while que[idx] > que[parent]:
        que[idx], que[parent] = que[parent], que[idx]
    idx = parent
    if idx//2 >= front:
        sort(idx)


def insert(x):
    que.append(x)
    idx = len(que)-1
    sort(idx)


def delete():
    global front
    if front >= len(que):
        sys.stdout.write('0\n')
    else:
        sys.stdout.write(str(que[front])+'\n')
        front += 1
        que[front] ,que[-1] = que[-1], que[front]
        sort(len(que)-1)

que = [0]
front = 1
N = int(sys.stdin.readline().strip())
for num in sys.stdin:
    num = int(num.strip())
    if num == 0:
        delete()
    else:
        insert(num)