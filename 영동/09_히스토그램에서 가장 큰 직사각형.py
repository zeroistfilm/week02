# https://www.acmicpc.net/problem/6549
# &1 메모리 초과 : Q: 메모리 초과가 나오는것은 리스트의 문제인가??
# https://bladejun.tistory.com/11 스택을 이용한  풀이



while True:
    N, *cols = list(map(int, input().split())) #*이 하나가 붙은 경우, 가변 변수로 설정한다.
    cols.append(0)
    if N==0:#종료조건
        break
    area=0
    stack = []#스택에 인덱스를 넣는

    for i, h in enumerate(cols): #인덱스와 값을 동시에 전달한다.
        #print(i,h)
        while stack and cols[stack[-1]]>h: #스텍 마지막에 쌓인 기둥이 현재 기둥보다 더 클 클때
            ih=cols[stack.pop()]#현재 높이
            w = i - stack[-1] - 1 if stack else i
            if area < w * ih: area = w * ih
        stack.append(i)
    print(area)















import sys

from collections import deque
#
#
# maxarea=0
# def divide_search(array):
#     start=0
#     end=len(array)
#     global maxarea
#
#     if len(array)==1:
#         area=array[0]
#         if area > maxarea:
#             maxarea = area
#         return 0
#     if len(array)<1:
#         return 0
#
#     minumumvalue=min(array)
#     mid = array.index(minumumvalue)  # 처음 케이스에서 인덱스 1이 반환됨
#     range=len(array)
#     area = minumumvalue*range
#     if area>maxarea:
#         maxarea=area
#     divide_search(array[start:mid])
#     divide_search(array[mid+1:end])
#
#
# while True:
#     testcase = list(map(int,sys.stdin.readline().split()))
#     N=testcase[0]
#     if N==0:
#         break
#     heights=testcase[1:]
#
#
#     divide_search(heights)
#     print(maxarea)







