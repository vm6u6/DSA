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

def nextPermutation( nums ):
    L = len(nums)
    min_v = 101; min_idx = 0

    for i in range( L-2, -1, -1 ):
        if nums[i]<nums[i+1]:
            idx = i
            print(idx)
            for j in range( idx, L ):
                print(j)
                if nums[j] > nums[idx] and nums[j] < min_v:
                    min_idx = j
                    min_v = nums[j]
                print(min_idx)
            break
    if min_v != 101:
        nums[min_idx], nums[idx] =  nums[idx], nums[min_idx] 
        quick_sort( nums, idx+1, L-1 )
    else:
        quick_sort( nums, 0, L-1 )
    return nums


# nums = [1,2,3]
# print( nextPermutation(nums) )  

# nums = [1,2]
# print( nextPermutation(nums) )

nums = [1,3,2]
# print( nextPermutation(nums) ) 
print( nextPermutation(nums) )