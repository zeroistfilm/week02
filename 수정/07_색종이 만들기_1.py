import sys

sys.stdin = open('text/07.txt','r')


N = int(input())

paper =[]

for i in range(N):
    paper.append(list(int(i) for i in input().split()))

blue = 0
white = 0

def checkBox(N):
    global blue
    global white
    p = [0, N//2, N]
    xp = [0, N//2, 0, N//2]
    yp = [0, 0, N//2, N//2]
    for i in range(4):
        y = yp[i]
        x = xp[i]
        num = paper[y][x]
        no = 0
        for m in range(p[i//2],p[(i+2)//2]):
            for k in range(p[i%2],p[(i+1)%2]): #
                if paper[m][k] != num:
                    no += 1
                    break
        if no != 0:
            checkBox(N//2)
        else:
            if num == 1:
                blue += 1
                print(str(x)+' '+str(y)+'b')
            else:
                white += 1
                print(str(x)+' '+str(y)+'w')


checkBox(N)

print(white)
print(blue)



