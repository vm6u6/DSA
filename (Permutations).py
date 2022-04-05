
# def recur_permu( nums, i, j, tmp, ans ):
#     tmp.append(nums[i])
#     if ( j == len(nums) ):
#         ans.append(tmp)
#         tmp = []
#         tmp.append(nums[i])
#         return ans
#     if ( nums[i] != nums[j] ):
#         # print(tmp)
#         tmp.append(nums[j])
#         recur_permu( nums, i, j+1, tmp, ans )
#         recur_permu( nums, i+1, j+1, tmp, ans )
#     else:
#         recur_permu( nums, i, j+1, tmp, ans )
#     return ans

# def permutations( nums ):
#     recur_permu( nums, i, j, tmp, ans )
#     return ans

# nums = [1, 2, 3]
# ans = []
# tmp = []
# j = 0
# i = 0
# if ( len(nums) == 1 ):
#     ans.append(nums)
#     print( ans )
# else:
#     print( permutations(nums) )


def recur( nums, ans, tmp, L ):
    if ( L == 0 ) and tmp not in ans:
        ans.append(tmp)
    for i in nums:
        idx = nums.index(i)
        nums.remove(i)
        recur( nums, ans, tmp+[i], L-1 )
        nums.insert(idx, i)
    return ans

def permutations( nums ):
    ans = []
    tmp = []
    L = len(nums)
    return recur( nums, ans, tmp, L )
    

nums = [1,2,3]
print( permutations(nums) )
a= []
print(a+[100])