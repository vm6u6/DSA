def isValid( s ):
        ans = []
        memo = { "(":")", "{":"}", "[":"]" }
        L = len(s)
        for i in range( L ):
            if s[i] not in memo:
                if L<2 or s[i] != memo[ans[-1]] :
                    return False
                else:
                    ans.pop()
            else:
                ans.append( s[i] ) 
                
        if ans != []:
            return False
        return True

s = "]"
print( isValid(s) )  