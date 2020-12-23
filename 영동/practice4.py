# https://programmers.co.kr/learn/courses/30/lessons/60060?language=python3
from bisect import bisect_right, bisect_left

def count_by_range(array, left, right):
    leftindex = bisect_left(array, left)
    rightindex = bisect_right(array, right)
    return rightindex - leftindex

array = [[] for _ in range(10001)]
reverse_array = [[] for _ in range(10001)]

def solution(words,queries):
    answer=[]

    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()

    for q in queries:
        if q[-1]=='?': #접미
            res = count_by_range(array[len(q)],q.replace('?','a'),q.replace('?','z'))
        else: #접두
            res = count_by_range(reverse_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

        answer.append(res)
    return  answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
