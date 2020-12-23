# [백준] https://www.acmicpc.net/problem/2504 괄호의 값
# 전체선택 + ctrl + alt + l

import sys

sys.stdin = open('text/18.txt')

str = list(input())
N = len(str)
stk = []
summ = 0
ans = 0
tmp = 0
if len(str) == 1:
    print(0)
    exit(0)

for i in range(N):
    l = len(stk)
    j = l - 1  # 'stk의 뒤에서 첫번째로 괄호인 인덱스'
    while j >= 0 and type(stk[j]) == int:
        j -= 1
    if '(' == str[i]:
        stk.append('(')

    elif '[' == str[i]:
        stk.append('[')

    elif l > 0 and j >= 0 and not stk[j] ==']' and not stk[j] ==')':


        if (')' == str[i] and stk[j] == '(') or (']' == str[i] and stk[j] == '['):
            for _ in range(l-j-1):
                summ += stk.pop()
            stk.pop()
            if summ == 0:
                summ =1
            if ')' == str[i]:
                summ *= 2
            else:
                summ *= 3
            stk.append(summ)
            summ = 0
    else:
        print(0)
        exit(0)
if '[' in stk or ']' in stk or '(' in stk or ')' in stk:
    print(0)
else:
    print(sum(stk))
# 괄호값 stk이 비었으면 + , 아니면 계산된 숫자 stk .pop * }값
