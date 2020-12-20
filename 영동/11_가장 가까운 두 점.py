# https://www.acmicpc.net/problem/2261

import sys


# 8
# 0 0
# 1 2
# 3 5
# 10 10
# 0 10
# 10 0
# 7 9
# 6 10

def get_distance(x1,y1,x2,y2):
    distance = (x2-x1)**2+(y2-y1)**2
    return distance

N = int(input())
points=[]
for i in range(N):
    points.append(list(map(int,input().split())))

points.sort(key=lambda x:(x[0],x[1]))
minimum=sys.maxsize

left=0

right=len(points)
mid=(left+right)//2

def get_minimumdistance(array):
    minimum,minindex=sys.maxsize,0
    for i in range(len(array)-1):
        distance = abs(array[i][0]-array[i+1][0])
        if minimum>distance:
            minimum=distance
            minindex=i #i와 i+1의 거리가 제일 적다
    return minindex


leftSideMinIndex= get_minimumdistance(points[left:mid])
rightSideMinIndex = get_minimumdistance(points[mid:right])

leftsideMinCoordi1 = [points[left:mid][leftSideMinIndex][0], points[left:mid][leftSideMinIndex][1]]
leftsideMinCoordi2 = [points[left:mid][leftSideMinIndex + 1][0], points[left:mid][leftSideMinIndex + 1][1]]
leftSiedeDistance = get_distance(leftsideMinCoordi1[0], leftsideMinCoordi1[1], leftsideMinCoordi2[0],leftsideMinCoordi2[1])

rightsideMinCoordi1 = [points[mid:right][rightSideMinIndex][0], points[mid:right][rightSideMinIndex][1]]
rightsideMinCoordi2 = [points[mid:right][rightSideMinIndex + 1][0], points[mid:right][rightSideMinIndex + 1][1]]
rightSiedeDistance = get_distance(rightsideMinCoordi1[0], rightsideMinCoordi1[1], rightsideMinCoordi2[0],
                                  rightsideMinCoordi2[1])

if rightSiedeDistance > leftSiedeDistance:
    offset = leftSiedeDistance
else:
    offset = rightSiedeDistance

midpartpoint = points[mid - offset:  mid + offset]

minDisResult=sys.maxsize
for i in range(len(midpartpoint)):
   # print(i, midpartpoint[i:])
    for j in range(1,len(midpartpoint[i:])):

        # print(i,j,midpartpoint[i:][0],midpartpoint[i:][j],get_distance(midpartpoint[i:][0][0],midpartpoint[i:][0][1],midpartpoint[i:][j][0],midpartpoint[i:][j][1]))
        caldis = get_distance(midpartpoint[i:][0][0],midpartpoint[i:][0][1],midpartpoint[i:][j][0],midpartpoint[i:][j][1])
        if minDisResult>caldis:
            minDisResult=caldis

print(minDisResult)





