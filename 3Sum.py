# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         L = len(nums)
#         ans = []
#         val = []

#         if ( nums == [] ) or ( L < 3 ):
#             return ans
#         sorted(nums)

#         for i in range( L-1 ):
#             for j in range( i+1, L ):
#                 tmp1 = nums[i]; tmp2 = nums[j]
#                 tmp = -(tmp1 + tmp2)
#                 nums.pop(i)
#                 nums.pop(j-1)
#                 if ( tmp in nums ):
#                     val = [ tmp1, tmp2, tmp ]
#                     val = sorted(val)
#                     if val not in ans:
#                         ans.append(val)
#                 nums.insert( i, tmp1 )
#                 nums.insert( j-1, tmp2 )               
#         return ans

def threeSum(nums):
    L = len(nums)
    ans = []
    if ( nums == [] ) or ( L < 3 ):
        return ans
    nums = sorted(nums)
    print(nums)

    for i in range( L-1 ):
        print("--START--") 
        val = []
        for j in range( i+1, L ):
            num1 = nums[i]; num2 = nums[j]
            print("num1:", num1)
            print("num2:", num2)
            print()
            if num2 in val:
                ans.append( [num1, num2, -num1-num2] )
            val.append( -num1-num2 )
    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
# nums = []
# print(threeSum(nums))
# nums = [0,1,-2]
# print(threeSum(nums))