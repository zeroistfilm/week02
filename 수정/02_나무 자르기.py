# https://www.acmicpc.net/problem/2805 나무자르기
import sys
sys.stdin = open('week02\\수정\\text\\02.txt', 'r')


N, M = map(int, input().split())
tree =list(map(int, input().split()))

low = 1
high = max(tree)

while low <= high:

	mid = (low+high)//2

	candM = 0
	for i in tree:	# 벌목된 나무의 총합
		if i > mid:
			candM = candM + i - mid

	if M > candM:	# 나무가 모자라면
		high = mid - 1
	elif M <= candM:	# 나무가 같거나 남으면
		low = mid + 1

print(high)	# high가 항상 엇갈리기 직전의 가장 긴 길이가 됨

