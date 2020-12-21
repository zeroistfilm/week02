# [백준] https://www.acmicpc.net/problem/18258
# 큐 구현
# [참고] https://chancoding.tistory.com/35
import sys
from sys import stdin
# sys.stdin = open('text/20.txt')
input()
que, com = [], stdin.readlines()

front = 0

for x in com:
    tmp = x.strip()
    if 'push' in tmp:
        tmp, n = tmp.split()
        que.append(n)
    elif 'pop' == tmp:
        if len(que) > front:
            print(que[front])
            front += 1
        else:
            sys.stdout.write('-1\n')
    elif 'size' == tmp:
        sys.stdout.write('%d\n' % (len(que)-front))
    elif 'empty' == tmp:
        if len(que) == front:
            sys.stdout.write('1\n')
            front = 0
            que = []
        else:
            sys.stdout.write('0\n')
    elif 'front' == tmp:
        if len(que) > front :
            print(que[front])
        else:
            sys.stdout.write('-1\n')
    elif 'back' == tmp:
        if len(que) > front:
            sys.stdout.write('%s\n' % que[-1])
        else:
            sys.stdout.write('-1\n')