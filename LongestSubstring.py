def longestsubstring( s ):
    sub = ""; ans = "a"
    L = len(s)
    if s == "":
        return 0

    for i in range( L ):
        
        if s[i] not in sub:
            sub = sub + s[i]
        else:
            sub = sub[sub.index(s[i])+1::] + s[i]
        
        if len(sub) >= len(ans):
            ans = sub

    return len(ans)

def longestsubstring2( s ):
    max_len = 0; tmp = ""
    if s == "":
        return 0

    for i in range( len(s) ):
        if s[i] not in tmp:
            tmp = tmp + s[i]
                
        elif s[i] in tmp:
            idx = tmp.index(s[i])
            tmp = tmp[idx+1::] + s[i]
        max_len = max( len(tmp), max_len )     
    return max_len

# s = "au"
# s = "pwwkew"
# s = "abcabcaa"
s = "dvdf"
print(longestsubstring(s))
print(longestsubstring2(s))