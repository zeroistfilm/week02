# 고정점 찾기
from bisect import bisect_left, bisect_right

nums=[-15,-6,1,3,7]

def check(array,num):
    if num == bisect_left(array, num):
        return True
i=0
while True:
    i+=1
    if i ==len(nums):
        print(-1)
        break
    if check(nums, nums[i])==True:
        print(i)
        break





