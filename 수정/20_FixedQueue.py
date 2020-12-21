# do it 알고리즘 큐 클래스 구현 실습


from typing import Any
import sys
sys.stdin = open('text/20.txt')
N = int(sys.stdin.readline().strip())

class FixedQueue:

    class Empty(Exception):
        pass


    class Full(Exception):
        pass


    def __init__(self, capacity: int) -> None:
        # 큐 초기화
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        # 큐에 있는 모든 데이터 개수를 반환
        return self.no


    def is_empty(self) -> bool:
        # 큐가 비어있는지 판단
        return self.no <= 0

    def is_full(self) -> bool:
        # 큐가 가득 차 있는지 판단
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        # 데이터 x를 인큐
        if self.is_full():
            raise FixedQueue.Full # 큐가 가득 차 있는 경우 예외처리 발생
        self.que[self.rear] = x
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        # 데이터를 디큐
        if self.is_empty():
            raise FixedQueue.Empty # 큐가 비어있는 경우 예외처리 발생
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
