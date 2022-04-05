

def IncreaseTriplet ( nums ):
    L = len(nums)
    Num1 =  2 ** 31
    Num2 =  2 ** 31
    for i in range ( L ):
        if ( nums[i] < Num1 ):
            Num1 = nums[i]
        if ( nums[i] > Num1 ):
            Num2 = min( nums[i], Num2 )
        if ( nums[i] > Num2 ):
            return True
    return False

nums = [1,2,3,4,5]
# nums = [5,4,3,2,1]
# nums = [20,100,10,12,5,13]
# nums = [20,100,10,200,12,3,13]
# nums = [0,4,2,1,0,-1,-3]
print( IncreaseTriplet(nums) )