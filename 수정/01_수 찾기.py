import sys
sys.stdin = open('week02/수정/text/01.txt', 'r')


n = int(input())
a = list(int(i) for i in input().split())
m = int(input())
b = list(int(i) for i in input().split())

n = 5
a= [4, 1, 5, 2, 3]
m = 5
b= [1, 3, 7, 9, 5]

list.sort(a)
# a는 검색할 리스트이므로 정렬해야함
# b는 원소를 가져와서 a에서 검색할 것이므로 정렬 필요X



for i in range(m):
	pl = 0
	pr = n - 1
	while True:
		mid = (pl+pr)//2
		if b[i] ==  a[mid]:
			print('1')
			break
		elif b[i] < a[mid]:
			pr = mid-1
		else:
			pl = mid+1
		if pl > pr:
			print('0')
			break
# pl = 0
# pr = n - 1
# while True:
# 	mid = (pl+pr)//2
# 	if b[0] ==  a[mid]:
# 		print('1')
# 		break
# 	elif b[0] < a[mid]:
# 		pr = mid-1
# 	else:
# 		pl = mid+1
# 	if pl > pr:
# 		break


