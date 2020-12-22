# [백준] https://www.acmicpc.net/problem/2493 탑

# 스택 안쓰고 풀어봤는데 런타임에러 뜸
# 검사한 tower중에서 이전에 검사한 것보다 큰 걸 저장하고 이전 것을 pop()하면 된다.
# stack을 안 쓰면 tower리스트에서 자기자신의 값과 같거나 큰 값을 발견할 때까지 계속 검사해야 하기 때문에
# 시간초과가 발생하였다.
import sys
sys.stdin = open('text/16.txt')
N = int(sys.stdin.readline().strip())

tower = list(map(int, sys.stdin.readline().split()))

sys.stdout.write('0 ')

for j in range(1, N):
    pointer = j-1
    while j > 0:
        if tower[pointer] < tower[j]:   #pointer에서 신호 못받음
            if pointer > 0:
                pointer -= 1
            else:
                sys.stdout.write('0 ')
                break
        else: #신호 받음
            sys.stdout.write(str(pointer+1)+ ' ')
            break
