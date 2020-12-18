from bisect import bisect_left, bisect_right

a=[[1, 4], [2, 2], [3, 3], [4, 5], [5, 1], [7, 2], [8, 4], [9, 4]]
x=6
ax=[]
for i in range(len(a)):
    ax.append(a[i][0])
print(ax)
print(bisect_left(ax,x))
print(bisect_right(ax,x))
