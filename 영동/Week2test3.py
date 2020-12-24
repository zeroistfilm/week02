# https://www.acmicpc.net/problem/2014

from itertools import combinations_with_replacement

K,N = map(int,input().split())
nums= list(map(int,input().split()))

# kC? = <27
tmp = list(combinations_with_replacement(nums,2))
result=[]
for i in range(len(tmp)):
    result.append(tmp[i][0]*tmp[i][1])

for i in range(len(nums)):
    result.append(nums[i])

result.sort()

print(result)