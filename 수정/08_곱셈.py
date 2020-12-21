# [백준] https://www.acmicpc.net/problem/1629 [곱셈]
# [참고] https://jjangsungwon.tistory.com/10

# 이 문제는 분할 정복 문제이다.
# A = 10, B = 11, C = 12라고 주어졌을 때 구해야 하는 정답은 10^11 % 12이다.
# 만약 10 * 10 * 10 * 10 ... * 10 % 12로 문제를 풀고자 했으면 시간 초과가 발생할 것이다.
# 시간 초과를 해결하기 위해서 곱셈의 개수를 줄이는 분할 정복이 필요하며 아래 과정을 중점적으로 구현하면 된다.

# 1. b의 값이 짝수인지 홀수인지 파악한다.
# 2. b의 값이 짝수라면 10 ^10 -> (10^5)^2 형태로 바꿔준다.
# 3. b의 값이 홀수라면 10 ^11 -> (10^5)^2 *10 형태로 바꿔준다.

# 10 ^ 11 % 12
# (10 ^ 5) ^ 2 * 10 % 12
# ((10 ^ 2) ^ 2 * 10) ^ 2 * 10 % 12
# 왜 곱셈의 개수가 줄지?
    # before => 10 * 10 ... 11번 + % 12 1번 =? 12번
    # after => 6번

def power(a,b):
    global C

    if b == 1:
        return a % C
    else:
        temp = power(a, b//2) # a^(b//2)를 미리 구한다.
        if b % 2 == 0: 
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C # b가 홀수일 때



A, B, C= map(int, input().split())


print(power(A, B))