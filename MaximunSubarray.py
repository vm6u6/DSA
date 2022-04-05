def maxSubArray(nums):
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            print(dp)
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)



nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [ 5,4,-1,7,8 ]
print(maxSubArray(nums))

# nums = [1,2]
# print(maxSubArray(nums))