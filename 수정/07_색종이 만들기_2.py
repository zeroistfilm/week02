import sys

sys.stdin = open('text/07.txt','r')


N = int(input())

paper =[]

for i in range(N):
    paper.append(list(int(i) for i in input().split()))

blue = 0
white = 0

def recur(x1, x2, y1, y2 ,N):
    global blue
    global white

    num = paper[y1][x1]
    no = 0
    for m in range(y1, y2):
        for k in range(x1, x2):
            if paper[m][k] != num:
                no += 1
                break
    if no != 0:
        if x2-x1 != 1 and y2-y1 != 1:
            checkBox(x1, y1, N//2)
    else:
        if num == 1:
            blue += 1
            print(str(x1) + ' ' + str(y1) + 'b')
        else:
            white += 1
            print(str(x1) + ' ' + str(y1) + 'w')


def checkBox(x, y, N):
    recur(x,x+N//2,y, y+N//2,N//2)
    recur(x+N//2,x+N,y,y+N//2,N//2)
    recur(x,x+N//2,y+N//2, y+N, N//2)
    recur(x+N//2,x+N,y+N//2,y+N, N//2)


checkBox(0,0,N)

print(white)
print(blue)



