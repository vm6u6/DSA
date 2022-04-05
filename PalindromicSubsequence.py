# recursion
def longestPalindrome( s ):

    start = 0; end = len(s)-1
    cnt = 0

    def helper( start, end, cnt, s ):
        print("HERE")
        print(start)
        print(end)
        if start == end:
            cnt = cnt + 1
            return cnt
        
        if start > end:
            return cnt
        
        else:
            if s[start] == s[end]:
                return helper( start+1, end-1, cnt+2, s )
            else:
                return max( helper( start+1, end, cnt, s ), helper( start, end-1, cnt, s ) )
    
    return helper( start, end, cnt, s )

# memo

def memo_longestPalindrome( s ):
    start = 0; end = len(s)-1
    cnt = 0
    memo = {}
    def helper( start, end, cnt, s ):
        print("HERE")
        print(memo)
        if start > end:
            return cnt

        if start == end:
            cnt = cnt + 1
            return cnt
    
        if (start, end) in memo:
            return memo[(start, end)]
        
        if s[start] == s[end]:
            memo[(start, end)] =  helper( start+1, end-1, cnt, s ) + 2
        else:
            memo[(start, end)] =  max( helper( start+1, end, cnt, s ), helper( start, end-1, cnt, s ) )
        return memo[(start, end)]
    return helper( start, end, cnt, s )

# DP
def dp_longestPalindrome( s ):
    L = len(s)
    ans = [[0] * L for _ in range( L )]
    
    for k in range( 1, L+1 ):
        for i in range( L-k+1 ):
            j = i + k - 1
            if i == j:
                ans[i][j] = 1
            elif s[i] == s[j]:
                ans[i][j] = ans[i+1][j-1] + 2
            else:
                ans[i][j] =  max(ans[i + 1][j], ans[i][j - 1])
    print(ans)
    return ans[0][-1]

# s = 'bbbab'
# s = 'avvd'
# s = 'aabaaba'
s = 'ababac'
print(memo_longestPalindrome(s))