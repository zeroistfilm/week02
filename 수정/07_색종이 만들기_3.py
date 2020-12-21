import sys

sys.stdin = open('text/07.txt')


N = int(input())

paper =[]

for i in range(N):
    paper.append(list(int(i) for i in input().split()))

blue = 0
white = 0


def recur(x, y, n):
    global paper
    global blue
    global white
    double_break = False
    num = paper[y][x]

    for m in range(y, y+n):

        if double_break:
            break

        for k in range(x, x+n):
            if paper[m][k] != num:
                recur(x, y, n//2)
                recur(x + n//2, y, n//2)
                recur(x, y+n//2, n//2)
                recur(x + n//2, y + n//2, n//2)
                double_break = True     #이 영역은 다 돌았다!
                break

    if not double_break:
        if num == 1:
            blue += 1
            print(str(x) + ' ' + str(y) + 'b')
        else:
            white += 1
            print(str(x) + ' ' + str(y) + 'w')


recur(0, 0, N)
print(white)
print(blue)



