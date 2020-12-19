# https://www.acmicpc.net/problem/1629

A,B,C = map(int,input().split())


def pow(x,m,C):

    if m==0:
        return 1

    else:
        tmp = pow(x, m // 2,C)
        if m%2==0: #짝수일경우
            return (tmp*tmp)%C
        else: #홀수일경우
            return (tmp*tmp)*x%C

print(pow(A,B,C))