import sys
n,k = map(int, input().split())
number=list(input().strip())
result=[]
tk=k

for i in range(n):
    while tk>0 and result and result[-1]<number[i]:
        del result[-1]
        tk-=1
    result.append(number[i])

print(''.join(result[:n-k]))


# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# s = list(input().strip())
# t, tk = [], k
# for i in range(n):
#     while tk > 0 and t and t[-1] < s[i]:
#         del t[-1]
#         tk -= 1
#     t.append(s[i])
# print(''.join(t[:n - k]))