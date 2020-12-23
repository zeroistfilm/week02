#정렬된 배열에서 특정 수의 개수 구하기

from bisect import bisect_left,bisect_right

#N,X = map(int, input().split())
# numbers=list(map(int,input().split()))
numbers=[1,3,3,3,4,5,6,7,2,2,2,3,3,3,4,4]
#이진탐색으로 특정 숫자 찾기
def count_by_range(list,leftvalue, rightvalue):
    rightindex = bisect_right(list, rightvalue)
    leftindex= bisect_left(list,leftvalue)
    return rightindex-leftindex

#print(count_by_range(numbers,X,X))
print(bisect_left(numbers,3))
print(bisect_right(numbers,3))
#bisect 정렬된 데이터에서 원하는 데이터의 위치를 찾는 함수
