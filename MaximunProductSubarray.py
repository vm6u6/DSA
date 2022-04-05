# def maxProduct(self, nums: List[int]) -> int:
#         L = len(nums)
#         tmp_idx = -1
#         Max = 1
#         total_max = -11
#         for i in range( L ):

#             if ( i == 0 ):
#                 Max = Max*nums[i]
#                 total_max = Max
#             elif ( nums[i] > Max ) and ( Max*nums[i]<nums[i] ):
#                 Max = nums[i]
#                 tmp_idx = i
#             elif ( Max*nums[i]>Max ):
#                 Max = Max*nums[i]
#                 tmp_idx = i

#             if ( i-1 != tmp_idx ):
#                 total_max = max( total_max, Max )
#                 Max = 1

#         return total_max 

# def maxProduct(nums):
#     L = len(nums)
#     if ( L == 1 ):
#         return nums[0]

#     Max = nums[0]
#     Min = nums[0]
#     total_max = -11
#     for i in range( 1, L ):
#         print("START")
#         if ( Min * nums[i] > Max * nums[i] ) and ( Min * nums[i] > nums[i] ) :
#             print("--Here1--")
#             Max = Min * nums[i]
#             Min = nums[i]
#         elif ( Max * nums[i] > Max ):
#             print("--Here2--")
#             Max = Max * nums[i]
#             Min = nums[i]
#         else:
#             print("--Here3--")
#             Min = Max * nums[i]
#             Max = max( Max, nums[i])


#         total_max = max( total_max, Max )
            
#         print("Max:", Max)
#         print("Min:", Min)
#         print("total max:", total_max)   
#         print()
#     return total_max

def maxProduct(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        N = len(nums)
        f = [0] * N
        g = [0] * N
        f[0] = g[0] = res = nums[0]
        for i in range(1, N):
            f[i] = max(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            g[i] = min(f[i - 1] * nums[i], nums[i], g[i - 1] * nums[i])
            res = max(res, f[i])
        return res


# nums = [2,-5,-2,-4,3]
# print(maxProduct(nums))
nums = [-1,-2,-9,-6]
print(maxProduct(nums))
# nums = [2]
# print(maxProduct(nums))
# nums = [-2,0,-1]
# print(maxProduct(nums))
# nums = [2,3,-2,4]
# print(maxProduct(nums))
# nums = [-3,-1,-1]
# print(maxProduct(nums))
# nums = [0,2]
# print(maxProduct(nums))
# nums = [-2,3,-4,-1]
# print(maxProduct(nums))
# nums = [-2,-3,-3,8]
# print(maxProduct(nums))
# nums = [3,2,-1,-2]
# print(maxProduct(nums))
