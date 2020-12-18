# https://www.acmicpc.net/problem/2630

N = int(input())
paper=[]
for i in range(N):
    paper.append(list(map(int,input().split())))

# 평균을 구l해서 1이면 파란종이 0이면 하얀종이

# print(paper)
count_blue=0
count_white=0

def split_paper(array,N):
    global count_blue, count_white

    papersum = 0
    for i in range(len(array)):
        papersum+=sum(array[i])

    if papersum/(N**2)==1:
        count_blue+=1
        return
    elif papersum/(N**2)==0:
        count_white+=1
        return
    else:
        #4등분하기
        Q1 = [row[0:N // 2] for row in array[0:N // 2]]
        Q2 = [row[N // 2:] for row in array[0:N // 2]]
        Q3 = [row[0:N // 2] for row in array[N // 2:]]
        Q4 = [row[0 + N // 2:] for row in array[N // 2:]]
        split_paper(Q1,N//2)
        split_paper(Q2,N//2)
        split_paper(Q3,N//2)
        split_paper(Q4,N//2)

split_paper(paper,N)
print(count_white,count_blue)