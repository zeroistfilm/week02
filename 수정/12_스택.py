import sys
sys.stdin = open('text/12.txt')
order = int(sys.stdin.readline().strip())

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
        print(stk.pop())
    else:
        print(-1)

def size():
    print(ptr)


def empty():
    if ptr == 0:
        print(1)
    else:
        print(0)


def top():
    if ptr != 0:
        print(stk[-1])
    else:
        print(-1)


for tmp in sys.stdin:
    if 'push' in tmp:
        tmp, num = tmp.split()
        push(num)
    elif 'pop' in tmp:
        pop()
    elif 'size' in tmp:
        size()
    elif 'empty' in tmp:
        empty()
    elif 'top' in tmp:
        top()



