import sys
sys.stdin = open('02.txt')

str = input()
str = list(str)
N = len(str)
stk = 0
pre = ''
answer = 0

for i in range(N):
    s = str[i]
    if '(' == s:
        stk += 1

    else:
        stk -= 1
        if pre == '(':   #레이저라면
            answer += stk
        else:
            answer += 1
    pre = s

print(answer)
