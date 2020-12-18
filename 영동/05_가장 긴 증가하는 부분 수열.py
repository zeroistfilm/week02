# https://www.acmicpc.net/problem/11053

# N = int(input())

N=6
# A = list(map(int,input().split()))
A = list(map(int,'10 20 10 30 20 50'.split()))

# 6
#

tmp=[]
count=0
hopping=1
def increse_sequence(Array,i):
    # 처음 건너뛰는 간격은 1이다
    global count, hopping
    if i+hopping>len(A)-1:# 마지막 인덱스에 도달 했을 때
        print(len(tmp))
        return
    if i==0:
        tmp.append(Array[i])
        i+=1
    else:
        if tmp[i-1]-Array[i+hopping] < 0:
            tmp.append(Array[i+hopping])
            count+=1
            hopping=1
            i += 1

        elif tmp[i-1]-Array[i+hopping] >= 0: #앞에서 뒤를 뺐는데 양수이다? 그럼 감소한것
            #증가 순열의 조건에 맞지 않음
            tmp.pop()
            #hopping +=1 # 건너뛰는 간격 증가


    increse_sequence(Array,i)

    #순차적으로 탐색을한다
    # i와 i+1의 차이가 양수이면 계속진행
    # 하지만 i+1과 i+2의 차이(1칸 간격)가 음수이면 i로 돌아가 문제를 다시 탐색한다.
    # 다시 탐색할때 i+1을 건너뛰고 i+2부터 (2칸간격후 1칸간격)다음을 탐색다

    #인덱스 증가

#0번 인덱스부터 진행
increse_sequence(A,0)
#d
# 10
# 1 100 2 3 4 5 6 7 8 9
# 6
# 10 20 10 30 20 50