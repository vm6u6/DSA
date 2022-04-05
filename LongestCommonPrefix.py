

def longestCommonPrefix(strs):

    if len(strs) == 1:
        return strs[0]

    L = 201
    for i in range(len(strs)):
        if ( len(strs[i]) < L ):
            L = len(strs[i])
            
    sol = ""
    for i in range(L):
        for j in range(len(strs)):
            if(strs[0][i] != strs[j][i]):
                return sol
        sol += strs[j][i]
    return sol

def longestCommonPrefix2( strs ):
    ans = ""
    strs = sorted(strs)
    for i in range( len(strs[0]) ):
        ans = ans + strs[0][i]
        for j in range( 1, len(strs) ):
            
            if ans != strs[j][:i]:
                print(strs[j][:i])
                print(ans)
                ans = ans[:-1]
                break
    return ans
               


strs = ["flower","flow","flight"]
# strs = ["reflower","flow","flight"]
print(longestCommonPrefix(strs))
print(longestCommonPrefix2(strs))
# strs = ["dog","racecar","car"]
# print(longestCommonPrefix(strs))

# strs = ["a"]
# print(longestCommonPrefix(strs))