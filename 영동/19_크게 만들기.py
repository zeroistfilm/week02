# https://www.acmicpc.net/problem/2812

#스택 정렬하는걸로는 안되나보다,,,,,

N,K = map(int,input().split())
number=input()

orgstk=[]
newstk=[]


for i in range(N):
    orgstk.append(int(number[i]))

newstk.append(orgstk.pop())
while len(orgstk)!=0: #새로운 스택이 비지 않을때까지
    tmp=orgstk.pop()
    if len(newstk)!=0 and tmp < newstk[len(newstk)-1]:
        #꺼내 놓은게 더 작으면
        while len(newstk)!=0:
            #newstk에 있는걸모두 org으로 옮긴다
            orgstk.append(newstk.pop())
    newstk.append(tmp)
result=''
for i in range(K):
    result+=str(newstk.pop())

print(int(result))
