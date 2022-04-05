def CombinationSum( candidates, target ):
    
    def helper( tmp, ans, idx, candidates, target ):

        if sum(tmp) == target:
            ans.append(tmp)
            return ans
        
        if sum(tmp) > target:
            return 

        for i in range( idx, len(candidates) ):
            helper( tmp+[candidates[i]], ans, i, candidates, target )

    ans = []
    helper( [], ans, 0, candidates, target )          
    return ans


candidates = [2,3,6,7]; target = 7
print(CombinationSum( candidates, target ))