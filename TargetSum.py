def recur( ans, tmp, idx ):
    print("--START--")

    L = len(nums)    
    if idx == L:
        if target == tmp:
            print(ans)
            ans = ans + 1
        return ans
            
    # plus
    tmp = tmp + nums[idx]
    ans = recur( ans, tmp, idx+1 )
    tmp = tmp - nums[idx]

    # minus
    tmp = tmp - nums[idx]
    ans = recur( ans, tmp, idx+1 )
            
    return ans 


def backtrack( idx, ans ):
    if idx == len(nums):
        if ans == target:
            return 1
        else:
            return 0
            
    if ( idx, ans ) in memo:
        return memo[ ( idx, ans ) ]
    
    memo[(idx,ans)] = ( backtrack( idx+1, ans+nums[idx] ) + backtrack( idx+1, ans-nums[idx] )  )
        
    return memo[ (idx, ans) ]
        
        
return backtrack( 0, 0 )

nums = [1,1,1,1,1]; target = 3     
print(DP(nums, target))  
