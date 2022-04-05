def longestConsecutive(nums):
        
        if len(nums) == 0:
            return 0
        
        s = set(nums)
        print(s)
        cnt = 1; ans = 0
        for i in s:
            if i-1 not in s:
                
                

nums = [-1, 0, 1]
print(longestConsecutive(nums))
