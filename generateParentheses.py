def generateParenthesis( n ):

    def backtrack(open, close, res):
            print(res)
            if open == 0 and close == 0:
                results.append(res)
                return
            
            if open != 0:
                backtrack(open - 1, close, res + '(')
            
            if close > open: 
                backtrack(open, close - 1, res + ')')
        
    results = []
    backtrack(n, n, '')
    return results


    

n = 3
print(generateParenthesis( n ))