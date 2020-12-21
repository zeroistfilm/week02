import sys

sys.stdin = open('text/20.txt')

N = int(sys.stdin.readline().strip())
stk = []
ptr = 0


def push(X):
    global ptr
    stk.append(X)
    ptr += 1


def pop():
    global ptr
    if ptr > 0:
        ptr -= 1
        return stk.pop()
    else:
        return -1

for height in sys.stdin:
    h = int(height.strip())
    push(h)

cnt = 1
last = pop()
for i in range(ptr):
    if stk[-1] > last:
        cnt += 1
        last = pop()
    elif stk[-1] <= last:
        pop()
print(cnt)