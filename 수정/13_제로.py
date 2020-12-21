# [백준] https://www.acmicpc.net/problem/10773
# 스택 실습
import sys

sys.stdin = open('text/13.txt')

K = int(sys.stdin.readline().strip())
stk = []
ans = 0
ptr = 0


def pop():
    global ans
    global ptr
    if ptr > 0:
        ans -= stk[-1]
        stk.pop()
        ptr -= 1
    return ans


def push(X):
    global ptr
    stk.append(X)
    ptr += 1


for line in sys.stdin:
    num = int(line.strip())
    if 0 == num:
        ans = pop()
    else:
        push(num)
        ans += num
print(ans)