# [백준] https://www.acmicpc.net/problem/2504 괄호의 값

# 다른 층위에 있는 +관계의 괄호들을 같은 summ이라는 리스트에 저장하면
# 문제가 해결되지 않는다.
# 하다가 괄호와 숫자를 하나의 스택에서 저장하면 어디까지가 같은 층위인지
# 헷갈릴 문제없이 계산가능하다는 얘기를 듣고 재도전 => 2
import sys
sys.stdin = open('text/18.txt')

str = list(input())
N = len(str)
stk = []
sigstk = []

ans = 0
summ = []
sig = 0
tmp = 0
if len(str) == 1:
    print(0)
    exit(0)

for i in range(N):
    if '(' == str[i]:

        summ.append(tmp)        # ) or ]
        tmp = 0
        stk.append(2)

    elif '[' == str[i]:
        summ.append(tmp)        # ) or ]
        tmp = 0
        stk.append(3)


    elif (len(stk) !=0) and ((')' == str[i] and stk[-1] ==2)
        or (']' == str[i] and stk[-1] ==3)):
        if tmp != 0:
            if len(summ) != 0:
                while summ[_] ==
                tmp += sum(summ[_][1])
                summ.clear()
            tmp = tmp * stk[-1]
            stk.pop()
        else:
            tmp = stk.pop()
    else:
        tmp = 0
        break
if len(stk) != 0:
    tmp = 0

print(tmp)
# 괄호값 stk이 비었으면 + , 아니면 계산된 숫자 stk .pop * }값
