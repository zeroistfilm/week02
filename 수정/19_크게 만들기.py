# [백준] https://www.acmicpc.net/problem/2812 크게만들기
# 스택 문제
# 숫자가 클 수록, 같은 수라면 앞에 있을 수록 남겨야 함
import sys
sys.stdin = open('text/19.txt')
N, M = list(map(int, input().split()))
num = input().strip()
K = N -M
# 첫 번째로 큰 수가 num[N-K]와 같거나 그보다 앞에 있지 않다면 일단 남김
# 뽑고나서 만약 뒤에 남은 원소가 앞으로 뽑아야 할 원소와 같다면 그대로 종료

# 숫자9부터 찾아서 0:N-K인덱스까지 확인
# 그 중 가장 큰 수 찾아서 (ex : i
# 그 수의 다음 인덱스부터 i+1 : N-K+1까지 확인

pick = []
ans = ''

# for i in range(9,0,-1):
i = 9
front = 0
while True:

    for j in range(front, N-K+1):
        if str(i) == num[j:j+1]:
            # pick.append(num[j])
            ans += num[j:j+1]
            front = j+1
            K -= 1
            if N - front== K:
                ans += num[front:]
                print(ans)
                exit(0)
            i = 9
            break
    else:
        i -= 1

    if K == 0:
        break
print(ans)
