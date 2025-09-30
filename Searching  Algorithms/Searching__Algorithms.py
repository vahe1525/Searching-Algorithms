import math


#Linear Search Algorithm 
def LinearSearch(col, key):
    for val in col:
        if val == key :
            return True
    return False


#Binary search Algorithm
def BinarySearch(col, key):
    col.Sort()

    eft, right = 0, len(col) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if col[mid] == key:
            return True
        elif col[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
    
    return False 
    
def Ternary_search(col, key):
    # col.Sort()

    left, right = 0, len(col) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if col[mid1] == key:
            return True
        if col[mid2] == key:
            return True
        if key < col[mid1]:
            right = mid1 - 1
        elif key > col[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return False


def JumpSearch(col, key):
    col.sort()
    n = len(col)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and col[min(step, n) - 1] < key:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return False

    for i in range(prev, min(step, n)):
        if col[i] == key:
            return True
    return False




collection = [i for i in range(10)]
key = 6
res = LinearSearch(collection, key)
res = Ternary_search(collection, key)
res = JumpSearch(collection, key)
print(res)
