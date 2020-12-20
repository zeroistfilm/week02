# https://www.acmicpc.net/problem/17608

N = int(input())

cols=[]
for i in range(N):
    cols.append(int(input()))

height=cols[len(cols)-1]
visable=[]
visable.append(height)

for i in range(len(cols)-2,-1,-1):
    # print(cols[i])
    if cols[i]>height:
        visable.append(cols[i])
        height=cols[i]


print(len(visable))




