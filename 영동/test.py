from bisect import bisect_left, bisect_right

N = 4
array = [[1, 1, 2, 2], [1, 1, 2, 2, ], [3, 3, 4, 4], [3, 3, 4, 4]]

# for i in range(N // 2 - 1):
#     Q1 = [a[i][:N // 2]], [a[i + 1][:N // 2]]
#     Q2 = [a[i][N // 2:]], [a[i + 1][N // 2:]]
#     Q3 = [a[i+N//2][:N // 2]], [a[i + 1+i+N//2][:N // 2]]
#     Q4 = [a[i+N//2][N // 2:]], [a[i + 1+i+N//2][N // 2:]]

Q1=[row[0:N//2] for row in array[0:N//2]]
Q2=[row[N//2:] for row in array[0:N//2]]
Q3=[row[0:N//2] for row in array[N//2:]]
Q4=[row[0+N//2:] for row in array[N//2:]]
print(Q1)
print(Q2)
print(Q3)
print(Q4)
