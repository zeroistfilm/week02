# https://www.acmicpc.net/problem/1992

N = int(input())
pixel=[]
pixels=[[0 for i in range(N)] for i in range(N)]
for i in range(N):
    arrystr=input()
    for j in range(N):
        pixels[i][j]=int(arrystr[j])

def split_img(array,N):

    pixcelsum = 0
    for i in range(len(array)):
        pixcelsum+=sum(array[i])

    if pixcelsum/(N**2)==1:
        print('1',end='')

        return
    elif pixcelsum/(N**2)==0:
        print('0',end='')

        return
    else:
        #4등분하기
        Q1 = [row[0:N // 2] for row in array[0:N // 2]]
        Q2 = [row[N // 2:] for row in array[0:N // 2]]
        Q3 = [row[0:N // 2] for row in array[N // 2:]]
        Q4 = [row[0 + N // 2:] for row in array[N // 2:]]
        print('(', end='')
        split_img(Q1,N//2)
        split_img(Q2,N//2)
        split_img(Q3,N//2)
        split_img(Q4,N//2)
        print(')', end='')

split_img(pixels,N)


