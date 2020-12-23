# [백준] https://www.acmicpc.net/problem/2493 탑
import sys
sys.stdin = open('text/16.txt')
N = int(sys.stdin.readline().strip())

tower = list(map(int, sys.stdin.readline().split()))
stk = []

sys.stdout.write('0 ')
stk.append(0)

for j in range(1, N):

    while stk and tower[stk[-1]] < tower[j]:
        stk.pop()
    if stk: # 비었다 => 0 출력
        print(stk[-1]+1, end=' ')
    else:
        print('0',end=' ')
    stk.append(j)



