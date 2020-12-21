import sys
sys.stdin = open('text/14.txt')
T = int(sys.stdin.readline().strip())


for line in sys.stdin:
    t = line.strip()
    t = list(t)
    left = 0
    right = 0
    for p in t:
        if p == '(':
            left += 1
        else:
            right += 1
            if right > left:
                break
    if left == right:
        print('YES')
    else:
        print('NO')