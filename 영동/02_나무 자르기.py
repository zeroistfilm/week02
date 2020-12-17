# https://www.acmicpc.net/problem/2805
import sys

numberoftree,needmeter = map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))
#tree.sort()


start =1
end=max(tree) #절단높이

while start<=end:
    mid=(start+end)//2

    #cut=[x-tree[mid] for x in tree[mid:]]

    cut = 0
    for i in tree:
        if i>=mid:
            cut+=i-mid
    if cut >= needmeter:
        start=mid+1
    else:
        end=mid-1


print(end)