# https://www.acmicpc.net/problem/2504


checklist=input()

stksmall=[]
stkmid=[]

A = []

tmp=1
result=0

beforevalue=''
for i in range(len(checklist)):

    if checklist[i] == '[':
        stkmid.append(checklist[i])
        tmp*=3
        beforevalue='['

    elif checklist[i] == ']':
        if beforevalue == '[':
            result+=tmp
        if len(stkmid)==0:
            break
        else:
            stkmid.pop()
            tmp /= 3
        beforevalue = ']'

    elif checklist[i] == '(':

        stkmid.append(checklist[i])
        tmp *= 2
        beforevalue = '('
    elif checklist[i] == ')':

        if beforevalue == '(':
            result+=tmp
        if len(stkmid)==0:
            break
        else:
            stkmid.pop()
            tmp /= 2
        beforevalue=')'

if len(stkmid)!=0 or len(stksmall)!=0:
    print(int(0))
else:
    print(int(result))
