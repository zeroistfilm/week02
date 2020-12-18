N = int(input())

paper =[]

for i in range(N):
    paper.append(list(int(i) for i in input().split()))

i = N
cnt =0
while True:
    if i == 1:
        break
    i /= 2
    cnt += 1


def checkBox(N):
    num = paper[0][0]
    for i in range(N):
        for j in range(N):
            if paper[i][j] != num:
                break



