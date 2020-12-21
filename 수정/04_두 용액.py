# https://0urtrees.tistory.com/92

# 무엇을 이분탐색할 것인가?? => 두 용액의 합??
# 투포인터 알고리즘으로도 풀 수 있다.

import sys

sys.stdin = open('week02\\수정\\text\\04.txt', 'r')

N = int(input())
P = list(map(int, sys.stdin.readline().split()))
P.sort()
ans = [P[0],P[-1]]

min = P[0] +P[-1]
for i in range(len(P)):
	low = i + 1				# i+1부터 탐색 시작
	high = N - 1

	while low <= high:
		mid = (low +high)//2
		ans = P[i] + P[mid]

		if abs(ans) < abs(min):		#최솟값 저장
			min = ans
			ans = [P[i], P[mid]]

		if ans < 0:
			low = mid + 1
		elif ans > 0:
			high = mid - 1
		else: # sum == 0
			print(str(P[i])+' '+str(P[mid]))
			exit(0)

print(str(ans[0])+' '+str(ans[1]))



