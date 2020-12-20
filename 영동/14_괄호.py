# https://www.acmicpc.net/problem/9012

N = int(input())

checks=[]
for i in range(N):
    checks.append(input().split())

def check(value):
    A = []
    for j in range(len(value)):
        if value[j] =='(':
            A.append(value[j])
        else:
            if len(A)!=0:
                A.pop()
            else:
                return print('NO')

    if len(A)!=0:
        return print('NO')
    else:
        return print('YES')




for i in checks:
    value=str(i[0])
    check(value)

