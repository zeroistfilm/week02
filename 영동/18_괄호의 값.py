# https://www.acmicpc.net/problem/2504


checklist=input()
#checklist="(()[[]])([])"

def check_brakcets(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')' and stack:
            if stack[-1] == '(':
                stack = stack[:-1]
            else:
                stack.append(s)
        elif s == ']' and stack:
            if stack[-1] == '[':
                stack = stack[:-1]
            else:
                stack.append(s)
        else:
            stack.append(s)
    if stack:
        return False
    else:
        return True



def sol(ss):
    stack = []
    for s in ss:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack[-1] == '(':
                stack[-1] = 2
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '(':
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
        elif s == ']':
            if stack[-1] == '[':
                stack[-1] = 3
            else:
                tmp = 0
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == '[':
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack[i]
                        stack = stack[:-1]
    return sum(stack)

if check_brakcets(checklist)==False:
    print(0)
else:
    print(sol(checklist))