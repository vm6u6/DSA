

def  backtrack_sub (idx, tmp):
    ans.append(tmp)
    for i in range( idx, len(nums) ):
        # tmp = tmp + [nums[i]]
        backtrack_sub( i+1, tmp + [nums[i]])
    return ans


ans = []  
nums = [1,2,3]
backtrack_sub(0, [])
print(ans)