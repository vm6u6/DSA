
def backtrack( nums, ans, tmp, idx ):
    
    print(tmp)
    if tmp not in ans:
        ans.append(tmp)

    for i in range(idx, len(nums)):

        backtrack( nums, ans, tmp+[nums[i]], i+1 )


ans = []; tmp = []; idx = 0
nums = [1,2,3]
backtrack( sorted(nums), ans, tmp, idx )
print(ans)