# https://www.acmicpc.net/problem/1629

A,B,C = map(int,input().split())


def pow(x,m):

    if m==0:
        return 1
    elif m==1:
        return x
    if m%2>0:#짝수
        return (pow(x,m/2))**2
    else: #홀수
        return (pow(x,m/2)**2)*x
