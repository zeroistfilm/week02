# https://www.acmicpc.net/problem/18258

from collections import deque
import sys
class queue():
    def __init__(self):
        self.queue=deque()

    def push(self,n):
        self.queue.append(n)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        else:
            return -1
    def size(self):
        return len(self.queue)

    def empty(self):
        if self.queue:
            return 0
        else:
            return 1

    def front(self):
        if not self.queue:
            return -1
        else:
            return self.queue[0]
    def back(self):
        if not self.queue:
            return -1
        else:
            return self.queue[-1]


queue=queue()
N = int(input())
orders=[]
for i in range(N):
    orders.append(list(map(str,sys.stdin.readline().split())))

for order in orders:
    if order[0]=='push':
        queue.push(order[1])
    elif order[0] == 'pop':
        print(queue.pop())
    elif order[0] == 'size':
        print(queue.size())
    elif order[0] == 'empty':
        print(queue.empty())
    elif order[0] == 'front':
        print(queue.front())
    elif order[0] == 'back':
        print(queue.back())
