def groupAnagrams( strs ):

    ans = []; memo = {}; L = len(strs)
    for i in range( L ):
        
        tmp = sorted(strs[i])
        join_name = ''
        for j in range( len(tmp) ):
            join_name = join_name + tmp[j]

        if join_name not in memo:
            memo[join_name] = [strs[i]]
        else:
            memo[join_name].append(strs[i])
    return list( memo.values() )



strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))