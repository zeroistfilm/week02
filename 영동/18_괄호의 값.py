# https://www.acmicpc.net/problem/2504


checklist=input()

stksmall=[]
stkmid=[]

A = []




for i in range(len(checklist)):
    if checklist[i] == '[':
        stkmid.append(checklist[i])

    elif checklist[i] == ']':
        if len(stkmid)==0:
            break
        else:
            stkmid.pop()

    elif checklist[i] == '(':
        stksmall.append(checklist[i])

    elif checklist[i] == ')':
        if len(stksmall)==0:
            break
        else:
            stksmall.pop()

if len(stkmid)!=0 or len(stksmall)!=0:
    print('NO')
else:
    print('YES')