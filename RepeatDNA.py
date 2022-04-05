def repeatedDNA ( s ):

    L = len(s); memo = {}; ans = []
    for i in range( L-10+1 ):
        tmp = s[i:i+10]
        if tmp not in memo:
            memo[tmp] = 1
        else:
            if tmp not in ans:
                ans.append(tmp)
    return ans


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTTAAAAACCCCC"
print(repeatedDNA(s))