# https://www.acmicpc.net/problem/10799

SL=input()
stk=[]
count=0
lasercount=0
steelcount=0
for i in range(len(SL)):
    debeg1=(SL[i])

    if SL[i]=='(':
        stk.append((SL[i],i))
        steelcount+=1

    elif SL[i]==')':
        #steel count


        if stk[-1][0]=='(' and stk[-1][1]==i-1: #레이저일때

            stk.pop()
            stk.append('L')
            steelcount-=1#스틸이 아니였
            lasercount+=1
            if len(stk)==1 and stk[-1]=='L':
                stk.pop()
                lasercount -= 1
            count += len(stk)-lasercount
        else:
            while stk[-1]=='L':
                stk.pop()
                lasercount-=1
            stk.pop()
            count+=1
            steelcount-=1

print(count)

