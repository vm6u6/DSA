
def findDuplicate(nums):
    L = len(nums)
    tmp = [None] * (L-1)
    for i in range( L ):
        idx = nums[i]
        if tmp[idx-1] != None:
            return idx
        else:
            tmp.pop(idx-1)    
            tmp.insert(idx-1, idx)

# nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(findDuplicate(nums))