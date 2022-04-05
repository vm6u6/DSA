
def lengthOFLIS( nums ):
    L = len(nums)
    sub = [nums[0]]
    for i in range( L ):
        if ( nums[i] > sub[-1] ):
            sub.append(nums[i])
        for j in range( len(sub) ):
            if ( nums[i] <= sub[j] ):   
                sub[j] = nums[i]
                break
    return len(sub)

# nums = [10,9,2,5,3,7,101,18]
# print(lengthOFLIS( nums ))
nums = [4,10,4,3,8,9]
print(lengthOFLIS( nums ))