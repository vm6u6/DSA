def predictwin( nums ):

    i = 0; j = len(nums)-1
    
    if j == 0 :
        return True

    def helper( i ,j ):
        print("here")
        print(i)
        print(j)
        if i == j:
            return nums[i]
        
        left = nums[i] - helper( i+1, j )
        right = nums[j] - helper( i, j-1 )
        return max( left, right )
        
    return True if helper( i, j ) >= 0 else False

nums = [0]
print(predictwin(nums))