# https://www.acmicpc.net/problem/2261


def get_distance(x1,y1,x2,y2):
    distance = (x2-x1)**2+(y2-y1)**2
    return distance

N = int(input())
points=[]
for i in range(N):
    points.append(list(map(int,input().split())))

points.sort(key=lambda x:x[0])
min=0
for i in range(len(points)-1):
    distance = abs(points[i][0]-points[i+1][0])
    if min>distance:
        min=distance
        minindex=i #i와 i+1의 거리가 제일 적다

print(points[i],points[i+1])

