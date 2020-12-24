# [제출 성공]
import sys
sys.stdin = open('01.txt')
N = int(input())
matrix = [ list(sys.stdin.readline().strip()) for _ in range(N)]

# 단위 영상이 0인지 1인지 파악
# 리턴하고 괄호로 감싸야 함.

def quarter_check(start_i,start_j,n):
    std = matrix[start_i][start_j]
    flag = True

    for i in range(start_i,start_i+n): # 스타트 지점부터 스타트+n 지점까지
        if not flag: # 공통되어 있으면
            break
        for j in range(start_j,start_j+n):
            if std != matrix[i][j] : # 단위 영상이 같은지 파악
                flag = False
                print("(",end="")
                quarter_check(start_i,start_j, n//2) # 1사분면 체크
                quarter_check(start_i,start_j+ (n//2), n//2) # 2사분면 체크
                quarter_check(start_i+(n//2),start_j, n//2) # 3사분면 체크
                quarter_check(start_i+(n//2),start_j+(n//2), n//2) # 4사분면 체크
                print(")", end="")
                break # 브레이크를 안하면 n이 0이되면서 계속 재귀가 돌아감

    if flag : # 0혹은 1로만 되어있으면
        # if int(std) >=0 : # 가장 마지막으로 가면 크기가 1인 원소의 값이 1인지 0인지도 체크하고, 크기가 1까지 가지 않더라도 다 같으면 1혹은 0이 될 것.
        print(std,end="")


quarter_check(0,0,N)

