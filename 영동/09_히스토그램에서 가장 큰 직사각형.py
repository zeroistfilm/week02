# https://www.acmicpc.net/problem/6549
# &1 메모리 초과 : Q: 메모리 초과가 나오는것은 리스트의 문제인가??
# https://bladejun.tistory.com/11 스택을 이용한  풀이
import sys
from collections import deque


maxarea=0
def divide_search(array):
    start=0
    end=len(array)
    global maxarea

    if len(array)==1:
        area=array[0]
        if area > maxarea:
            maxarea = area
        return 0
    if len(array)<1:
        return 0

    minumumvalue=min(array)
    mid = array.index(minumumvalue)  # 처음 케이스에서 인덱스 1이 반환됨
    range=len(array)
    area = minumumvalue*range
    if area>maxarea:
        maxarea=area
    divide_search(array[start:mid])
    divide_search(array[mid+1:end])


while True:
    testcase = list(map(int,sys.stdin.readline().split()))
    N=testcase[0]
    if N==0:
        break
    heights=testcase[1:]


    divide_search(heights)
    print(maxarea)







