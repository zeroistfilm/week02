# https://www.acmicpc.net/problem/10828

N = int(input())


class stack():

    def __init__(self):
        self.stk=[]

    def push(self,n):
        return self.stk.append(n)

    def pop(self):
        if len(self.stk)==0:
            return -1
        else:
            return self.stk.pop()

    def size(self):
        return len(self.stk)

    def empty(self):
        #is_empty
        if len(self.stk)==0:
            return 1
        else:
            return 0

    def top(self):

        if len(self.stk)==0:
            return -1
        else:
            return self.stk[-1]

orders=[]
for _ in range(N):
    orders.append(list(input().split()))

# print(orders)

stk = stack()
for order in orders:

    if order[0]=='push':
        stk.push(order[1])
    elif order[0]=='pop':
        print(stk.pop())
    elif order[0] == 'size':
        print(stk.size())
    elif order[0] == 'empty':
        print(stk.empty())
    elif order[0] == 'top':
        print(stk.top())
