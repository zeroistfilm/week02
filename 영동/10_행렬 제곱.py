## https://www.acmicpc.net/problem/10830
#https://hooongs.tistory.com/114

N,B = map(int,input().split())

matrix=[]
for i in range(N):
    matrix.append(list(map(int,input().split())))

def mul(n,matrix1,matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= 1000

    return result


def devide(n,b,matrix):
    if b==1:
        return matrix
    elif b==2:
        return mul(n,matrix,matrix)
    else:
        tmp = devide(n,b//2,matrix)
        if b%2==0:
            return mul(n,tmp,tmp)
        else:
            return mul(n,mul(n,tmp,tmp),matrix)
    # 홀수 일 때 A ^ 11 = A ^ 10 * A ^ 10 * A ^ 1
    # 짝수 일 때 A ^ 8 = A ^ 4 * A ^ 4


result=devide(N,B,matrix)
for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()