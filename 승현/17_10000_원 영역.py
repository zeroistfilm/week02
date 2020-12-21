import sys
N = int(sys.stdin.readline())

list1 = []
for i in range(N):
    x,r = map(int,sys.stdin.readline().split())
    list1.append([x-r,-1])
    list1.append([x + r, 1])

list1.sort(key=lambda x:(x[0],-x[1])) #정렬 
