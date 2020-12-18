import sys
sys.stdin = open('week02\\수정\\text\\03.txt','r')

N,C = map(int, sys.stdin.readline().split())
address =[int(sys.stdin.readline()) for _ in range(N)]
address.sort()

# 방법을 찾아서 재도전

# 1. 공유기를 0번에 설치
# 2. 가장 가까운 공유기 사이의 간격을 설정 => 최소거리:1 + 최대거리:(Last-first))//2

# 3. 설정한 간격대로 공유기 설치() 후 설치된 공유기의 갯수를 체크한다.
# 4.  - 공유기가 모자라면 간격을 늘린다.
#	  - 공유기가 넘치면 간격을 줄인다. (정답이 될 여지가 있으므로 일단 저장후 계속한다.)


low = 0
high = address[-1] - address[0]

while low <= high:
	mid = (low+high) //2
	answer = 1			# 0번에 설치된 수 하나
	here = address[0]
	for i in range(1,N):
		if address[i] - here >= mid:
			here = address[i]
			answer += 1
	if answer < C:
		high = mid-1
	else: # answer >= C:
		low = mid+1
print(high)






