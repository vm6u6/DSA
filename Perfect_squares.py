

def perfect( n ):
    if n == 1:
        return 1

    # test the length
    L = 0
    for i in range( 2, 10**4 ):
        if i**2 == n:
            L = i
            break
        elif i**2 > n:
            L = i-1
            break

    print(L)
    # find square
    def backtrack( n, tmp, ans, idx ):

        if n == 0:
            ans.append(tmp)
            return 
                
        if n < 0:
            return
                
        for i in range( idx, L+1 ):  
            val = i**2

            backtrack( n-val, tmp+1, ans, i )
  
    ans = []; tmp = 0; idx = 1 
    backtrack( n, tmp, ans, idx )
    print(min(ans))

n = 141
perfect( n )
