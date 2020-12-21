# [백준] https://www.acmicpc.net/problem/18258
# 큐 구현
import sys

N = int(sys.stdin.readline().strip())

que = []
no = 0
front = 0
rear = 0
capacity = 1000

for line in sys.stdin:
    tmp = line.strip()
    if 'push' in tmp:
        tmp, n = tmp.split()
        que.insert(rear, n)
        no += 1
        rear += 1
        if rear == capacity:
            rear = 0

    elif 'pop' in tmp:
        if no <= 0:
            sys.stdout.write('-1\n')
        else:
            print(que[front])
            que[front] = None
            no -= 1
            front += 1
            if front == capacity:
                front = 0
    elif 'size' in tmp:
        sys.stdout.write('%d\n' % no)
    elif 'empty' in tmp:
        if no <= 0:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif 'front' in tmp:
        if no != 0:
            print(que[front])

        else:
            sys.stdout.write('-1\n')
    else:
        if no != 0:
            sys.stdout.write('%s\n' % que[rear - 1])
        else:
            sys.stdout.write('-1\n')