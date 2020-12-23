# [백준] https://www.acmicpc.net/problem/11053 가장 긴 증가하는 부분 수열
# 일단 재귀식으로 풀어보기
# 이분탐색 어떻게 할 지 모르겠다

import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

def recur():

    if A[i] < A[i-1]:









