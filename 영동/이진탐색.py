array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]

def binary_search(array,target,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if array[mid]==target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)


target=3
result=binary_search(array,target,0,len(array)-1)

print(result) # Return index
