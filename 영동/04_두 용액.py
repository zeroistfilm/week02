# https://www.acmicpc.net/problem/2470
import sys
N = int(input())

liquid=list(map(int,input().split()))
# 7
# -99 98 100 101 -2 -1 1

liquid.sort()
# -99 -2 -1 1 98 100 101
left  = 0
right = len(liquid)-1
al=0
ar=0
result=sys.maxsize
resultal=0
resultar=0

# -99 -2 -1 1 98 100 101
while left<right:#인덱스가 겹치면 같은값을 더한 결과가 출력된다

    al = liquid[left] #인덱싱하며 가장 왼쪽
    ar = liquid[right] #가장 오른쪽 값을 구한다
    tmp =al+ar #그 값을 더한다, 첫번째 케이스의 경우 101+(-99) = 2가 나온다

    if abs(tmp) < abs(result): #더한 결과의 절대값 (2)가 기존에 있던 결과보다 작을 경우 조건문 실행
        result=tmp #기존의 값보다 더 작은 값을 결과에 집어 넣는다

        # 결과에 저장할때 사용된 수를 저장한다, 문제의 조건에는 오름차순으로 출력하라고 나오는데
        # 이미 조건리스트가 정렬되어 있으므로 왼쪽이 더 작은 값을 갖는다
        resultal = liquid[left] #sum에 사용된 값을 저장한다
        resultar = liquid[right]


    # 일반적인 경우 sum값이 음수와 양수가 번갈아 나오게 되는데,
    # 결국 인덱싱을 검사하게 되는 것이다.
    # (이진 탐색이라그래서 건너뛰는거 생각했다가 이해가 정말 안됐다.)

    # sum값이 0보다 작을경우는 예외적으로 음수만 더해진경우가 존재한다.
    if tmp <=0:
        #만약 모든 용액의 값이 음수이면 left인덱스를 +1(우측으로이동)할경우, 최종 sum값이 줄어든다.
        # 결국 우리가 찾고자 하는 sum이 0에 가까워 지는 경우를 구할 수 있다.
        left+=1
    else:
        # 반대로 모든 용액의 값이 양수인경우에도 좌측으로 이동할 수록 sum이 0에 가까워진다.
        right-=1

print(resultal,resultar)









