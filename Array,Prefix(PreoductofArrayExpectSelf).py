class Solution:
    def productExceptSelf(self, nums):
        L = len(nums)
        tmp = []
        tmp.append(1)
        for i in range( L-1 ):
            tmp.append(tmp[i]*nums[i])
        
        tmp2 = []
        nums.reverse()
        tmp2.append(1)
        for i in range( L-1 ):
            tmp2.append(tmp2[i]*nums[i])
        tmp2.reverse()
        
        ans = []
        for i in range( L ):
            ans.append(tmp[i]*tmp2[i])
        return ans