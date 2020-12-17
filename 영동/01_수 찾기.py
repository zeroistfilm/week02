# https://www.acmicpc.net/problem/1920

N = int(input())

base=list(map(int,input().split()))

M= int(input())
trys=list(map(int,input().split()))

#sort는 함수를 쓰자
base.sort()

#이진탐색하기
def binary_search(N):
    left = 0
    right = len(base)-1

    while (left <= right):
        mid = int((left + right) /2)

        if base[mid] > N:
            right = mid - 1
        elif base[mid] < N:
            left = mid + 1
        else:
            return True


for i in trys:
    if binary_search(i)==True:
        print(1)
    else:
        print(0)
