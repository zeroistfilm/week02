# https://www.acmicpc.net/problem/2493

N = int(input())

towers=list(map(int,input().split()))

stk=[] #최대값 저장 스택
answer=[] #수신탑 인덱스 저장


for i in range(N):
    while stk: #스텍의 값이 존재한다면
        if stk[-1][1] > towers[i]: #스텍에 넣어진 마지막 값(가장 높은 탑의 높이) VS 현재 탑의 높이
            answer.append(stk[-1][0]+1) #현재 탑의 신호는 이미 넣어진 탑이 수신한다.
            break
        else:
            stk.pop() #스텍에 있는 가장 높은 탑보다 현재 탑의 높이가 클경우 기존에 있던 가장큰 탑 정보를 제거한다
    if not stk: #스텍의 값이 존재하지 않는다면
        answer.append(0) #출력할 답을 저장한다.
    stk.append([i,towers[i]]) #인덱스와 타워 높이를 넣어준다.


print(" ".join(map(str,answer)))







#
# def receive_signal(array,index,currenttower):
#     # print(array[:index])
#     for i in range(len(array[:index])-1,-1,-1):
#         if array[i]>=currenttower:
#             return i+1
#
#     return 0
#
# # 오른쪽 타워부터 선택을한다
# # 앞 타워부터 검색을 하는데 현재 타워보다 같거나 클 경우에만 수신할 수 있다.
# # 수신을 하면 수신된 타워의 인덱스를 반환한다. (인덱스로 타워를 선택해야 할 듯)
# # 그렇지 못하면 0을 반환
#
#
#
# for i in range(len(towers)-1,-1,-1):
#     print(receive_signal(towers,i,towers[i]))


