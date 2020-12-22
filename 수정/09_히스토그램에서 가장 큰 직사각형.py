# [백준] https://www.acmicpc.net/problem/6549 히스토그램에서 가장 큰 직사각형
# [참고] https://kyunstudio.tistory.com/102
# [참고2] https://kunkunwoo.tistory.com/71

import sys
sys.stdin = open('text/09.txt')


def solve(left, right):
    # 리턴 조건: 한칸이라면?
    if left == right:
        return case[left]

    # 두 칸 이상 : 왼쪽 / 오른쪽으로 나눠서 분할계산
    mid = (left + right) // 2
    lo = mid
    hi = mid + 1
    ret = max(solve(left, mid), solve(mid + 1, right))

    # 초기값 hi와 lo로 일단 두 칸짜리 사각형을 더함
    height = min(case[lo], case[hi])
    ret = max(ret, height * 2)


    while left < lo or hi < right:   # width가 left와 right에 도달할때까지 계속
        if hi < right and (lo == left or case[lo - 1] < case[hi + 1]):   #hi가 righ에 도달하지 않음 + (lo가 왼쪽에 도달했거나 lo 다음 값보다 hi 다음 값이 큼)
            hi += 1     # right쪽으로 이동
            height = min(height, case[hi])
        else :          # left 쪽으로 이동
            lo -= 1
            height = min(height, case[lo])
        ret = max(ret, height*(hi-lo+1))
    return ret

    print(case)


while True:
    case = list(map(int, sys.stdin.readline().split()))
    N = case[0]
    del case[0]
    if N == 0:
        break
    else:
        start = 0  # 왼쪽 마지막 인덱스
        end = len(case) - 1  # 오른쪽 마지막인덱스
        print(solve(start, end))


