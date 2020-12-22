class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 단, 링크드 리스트에 항상 노드가 있다고 가정한다"""
        # 코드를 쓰세요
        if self.head and self.tail is None:
            return None
            """마지막 노드일때"""

        new_head = self.head.next
        old_head = self.head
        self.head.next = None
        self.head = new_head
        return old_head.data

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)  # 새로운 노드를 만든다

        # 링크드 리스트가 비었는지 확인
        if self.head is None:
            self.tail = new_node
        else:
            new_node.next = self.head  # 새로운 노드의 다음 노드를 head 노드로 정해주고

        self.head = new_node  # 리스트의 head_node를 새롭게 삽입한 노드로 정해준다

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 여러 데이터를 링크드 리스트 앞에 추가
linked_list.prepend(11)
linked_list.prepend(7)
linked_list.prepend(5)
linked_list.prepend(3)
linked_list.prepend(2)

# 가장 앞 노드 계속 삭제
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())
print(linked_list.pop_left())

print(linked_list)  # 링크드 리스트 출력
print(linked_list.head)
print(linked_list.tail)


# class Node:
#     """링크드 리스트의 노드 클래스"""
#
#     def __init__(self, data):
#         self.data = data  # 노드가 저장하는 데이터
#         self.next = None  # 다음 노드에 대한 래퍼런스
#
#
# class LinkedList:
#     """링크드 리스트 클래스"""
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self, data):
#         """링크드 리스트 추가 연산 메소드"""
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node #테일의 마지막을 새로운 노드로 할당하고
#             self.tail = new_node #그 노드를 테일로 지정한다
#
#     def __str__(self):
#         res_str="|"
#         #링크드리스트를 돌기 위해 맨처음 노드를 설정해준다
#         iterator = self.head
#         while iterator is not None:
#             res_str +=f" {iterator.data} |"
#             iterator = iterator.next
#
#         return res_str
#
#     def find_node_at(self,index):
#         """링크드 리스트 접근 연산 메소드, 파라미터인덱스는 항상 있다고 가정"""
#         iterator = self.head
#         for _ in range(index):
#             iterator = iterator.next
#
#         return iterator
#
#     def find_node_with_data(self, data):
#         """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
#         # 코드를 쓰세요
#         iterator = self.head
#         while iterator is not None:
#             if iterator.data == data:
#                 return iterator
#             else:
#                 iterator = iterator.next
#
#
#     def insert_after(self,previous_node,data):
#         """링크드 리스트 주어진 노드 뒤 삽인 연산 메소드"""
#         new_node = Node(data)
#         if previous_node is self.tail:
#             self.tail.next = new_node
#             self.tail = new_node
#         else:
#             new_node.next = previous_node.next
#             previous_node.next = new_node
#
#     def prepend(self, data):
#         """링크드 리스트의 가장 앞에 데이터 삽입"""
#         new_node = Node(data)  # 새로운 노드를 만든다
#
#         # 링크드 리스트가 비었는지 확인
#         if self.head is None:
#             # 새 노드를 링크드 리스트의 유일한 노드로 만들어준다
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head  # 새로운 노드의 다음 노드를 head 노드로 정해주고
#             self.head = new_node  # 리스트의 head_node를 새롭게 삽입한 노드로 정해준다
#
#         #새로운 링크드 리스트 생성
# my_list = LinkedList()
#
# my_list.append(2)
# my_list.append(3)
# my_list.append(5)
# my_list.append(7)
# my_list.append(11)
#
# # print(my_list.find_node_at(4).data)
# # my_list.find_node_at(4).data=13
# print(my_list)
#
# node_2 = my_list.find_node_at(2)
# my_list.insert_after(node_2,6)
# print(my_list)
#
# head_node = my_list.head
# my_list.insert_after(head_node,9)
# print(my_list)