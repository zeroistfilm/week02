# https://www.acmicpc.net/problem/10773


N = int(input())

orders=[]
for i in range(N):
    orders.append(int(input()))

result=[]
for i in orders:

    if i==0:
        result.pop()
    else:
        result.append(i)

print(sum(result))