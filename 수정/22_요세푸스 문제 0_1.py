# 동적 프로그래밍[Dynamic programming]으로도 해결할 수 있음
# => [참고] https://statkclee.github.io/r-algorithm/r-josephus-problem.html
import sys

N, K = map(int, input().split())


cnt = 0
front = 0
que = []
ans = []

def put():
    print('<',end='')
    for i in range(len(ans)-1):
        sys.stdout.write(str(ans[i])+', ')
    sys.stdout.write(str(ans[-1])+'>\n')


for i in range(1,N+1):
    que.append(i)


while len(ans) < N:
    for i in range(front, len(que)):       #리스트 인덱스 기준! (실제 값 기준X)
        cnt += 1

        if cnt == K:
            cnt = 0
            ans.append(que[i])
            del que[i]
            front = i
            break
        if front == len(que)-1:
            front = 0
    if front == len(que): front = 0
put()
