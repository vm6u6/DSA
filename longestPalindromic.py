def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        
        def moveTillNotPalindrome( l, r, s ):
            while l>=0 and r<len(s):
                if s[l] == s[r]:
                    l-=1
                    r+=1
                else:
                    break
            return l,r
    
        x = 0; y = 0
        for i in range(len(s)):
            #This is for odd check, Taking single element as mid point here
            l, r = moveTillNotPalindrome( i, i, s )            
            print(l)
            print(r)
            #this to check if current substring is bigger than previously stored one.
            if r-l-1 > y-x:
                x = l+1
                y = r
            
            #this is for even check, taking two elements as mid points
            l, r = moveTillNotPalindrome( i-1, i, s) 
            
            if r-l-1 > y-x:
                x = l+1
                y = r
        
        return s[x:y]

s = "cbcd"
print(longestPalindrome(s))