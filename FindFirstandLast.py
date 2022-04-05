# def searchRange(self, nums: List[int], target: int) -> List[int]:
        
#     l = 0
#     r = len(nums) - 1
#     ans = [ -1, -1 ]
#     mid = 0
#     while l <= r:
#         mid = (l+r)//2
#         if nums[mid] == target:
#             ans[0] = mid
#             ans[1] = mid
#             break
#         if nums[mid] > target:
#             r = mid -1
#         if nums[mid] < target:
#             l = mid + 1
            
#     if ans[0] != -1:
#         while ans[0] >= 1 and nums[ans[0]-1] == target:
#             ans[0] = ans[0] - 1
#         while ans[1] < len(nums) - 1 and nums[ans[1] + 1] == target:
#             ans[1] = ans[1] + 1
#     return ans

def searchRange2( nums, target ):
    def BS_left( nums, target ):
           
        l = 0; r = len(nums) - 1
        while ( l <= r ):
            mid = (l + r)//2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        
    def BS_right( nums, target ):
            
        l = 0; r = len(nums) - 1
        while ( l <= r ):
            mid = (l + r)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r
    
    F = BS_left( nums, target )
    S = BS_right( nums, target )
    print(F)
    print(S)
    if F >= 0 and S >= 0:
        return [F, S]
    else:
        return [-1, -1]

nums = [5,7,7,8,8,10]
target = 8
nums = [5,7,7,8,8,10]
target = 6
nums = []
target = 0
# nums = [1]
# target = 1
print(searchRange2( nums, target ))