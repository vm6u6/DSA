# util
def swap( a, b ):
    return b, a

# bubble sort
# O(n^2)
# 用兩個for loop，第一個for loop是要比較的長度，第二個for loop只會經過i的長度
# 每一次比較都會把剩餘數列最大的移動到最右邊
def bubble_sort( a, size ):

    for i in range( size-1, 0, -1 ):
        for j in range( i ):
            if a[j] > a[j+1]:
                a[j], a[j+1] = swap( a[j], a[j+1] )
    return a

# insert sort
# O(n^2)
# 先取一個key，key為數列第二個數，把比key還要大的都放往右邊移動
def insert_sort( a, size ):
    for i in range( 1, size ):
        key = a[i]
        j = i -1
        while( key < a[j] and j >= 0 ):
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key
    return a

# selection sort
# O(n^2)
# 找每個subarray的最小值，與第一個交換
def selection_sort( a, size ):
    for i in range( size ):
        min_idx = i
        for j in range( i+1, size ):
            min_idx = min( a[min_idx], a[j] )
        swap(a[i], a[min_idx])
    return a

# heap sort
# O(nlogn)
# 排序的陣列製作成「最小堆積」(Min Heap)或是「最大堆積」(Max Heap)。
def heapify( a, length, root ):
    left = root*2 + 1
    right = root*2 + 2 
    largest = root # root

    if left < length and a[left] > a[largest]:
        largest = left
    if right < length and a[right] > a[right]:
        largest = right
    if ( largest != root ):
        swap( a[root], a[largest] )
        heapify( a, length, largest )

def heap_sort( a, size ):
    # max heap preparation
    for i in range( size//2-1, 0, -1 ):
        heapify( a, size, i )
    # switch the root with the last element
    for i in range( size-1, 0, -1 ):
        swap( a[i], a[0] )
        heapify( a, i ,0 )
    return a

# quick sort
# O(nlongn)
# divide and conquer 的一種
def partition (a, front, end):
    pivot = a[end]
    i = front - 1 
    for j in range( front, end ):
        if a[j] < pivot:
            i = i+1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[end] = a[end], a[i+1]
    return i+1

def quick_sort( a, front, end ):
    if front < end:
        pivot = partition( a, front, end)
        quick_sort( a, front, pivot-1 )
        quick_sort( a, pivot+1, end )
    return a
#--
def quick_sort2( a, front, end ):
    if front >= end:
        return 

    i = front
    j = end
    pivot = a[front]

    while ( i != j ):
        print(a)
        
        while a[j] > pivot and i < j:
            j = j - 1
        while a[i] <= pivot and i < j:
            i = i + 1
        print("i:", i)
        print("j:", j)
        if i < j:
            a[i], a[j] = a[j], a[i]
        
    a[front] = a[i]
    a[i] = pivot
    
    quick_sort2( a, front, i-1 )
    quick_sort2( a, i+1, end )
    return a

# merge sort
# O(nlogn)
# divide and conquer 的一種
def merge( left, right ):
    result = []

    while len(left) and len(right):
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result = result+left if len(left) else result+right
    return result

def mergeSort( array ):

    if len(array) < 2:
        return array

    mid = len(array)//2
    leftArray = array[:mid]
    rightArray = array[mid:]

    return merge(mergeSort(leftArray),mergeSort(rightArray))


a = [ 5,4,1,2,6,3,8,0,9,9 ]
size = len(a)
# print("--[bubble sort]--")
# print(bubble_sort( a, size ))
# print()
# print("--[insert sort]--")
# print(insert_sort( a, size ))
# print()
# print("--[selection sort]--")
# print(selection_sort( a, size ))
# print()
# print("--[heap sort]--")
# print(heap_sort( a, size ))
# print()
# print("--[quick sort]--")
# print(quick_sort( a, 0, size-1 ))
# print()
print(quick_sort2( a, 0, size-1 ))
print()
# print("--[merge sort]--")
# print(mergeSort( a ))