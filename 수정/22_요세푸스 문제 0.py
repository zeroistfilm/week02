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
    sys.stdout.write(str(ans[-1])+'>')

for i in range(1,N+1):
    que.append(i)

while True:
    for i in range(front, len(que)):       #리스트 인덱스 기준! (실제 값 기준X)
        cnt += 1

        if cnt == K :
            front = i+1
            cnt = 0
            ans.append(que[i])
            print(que)
            break
        que.append((que[i]))
    if len(que) - front < K:
        # for j in range(len(que)-1, front-1, -1):
        while True:
            if len(que)-front == 1:
                break
            tmp = K % (len(que)-front)
            if tmp != 0:
                ans.append((que[front+tmp-1]))
            else:
                ans.append(que[len(que)-front-1])
            front = front+1
        # put()
        print(ans)
        break
    # elif front == len(que) - 1:
    #     ans.append(que[front])
    #     print(ans)
    #     break
