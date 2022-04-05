# recursion
def recur_climbstairs( n ):
    if n == 0:
        return 1
    val = recur_climbstairs( n-1 )
    if n > 1:
        val = val + recur_climbstairs( n-2 )
    return val
# dp
def dp_climbstairs( n ):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    res = []
    res.append(1)
    res.append(2)
    for i in range( 2, n ):
        res.append(res[i-1] + res[i-2])
    return res[-1]



n = 38
print(dp_climbstairs( n ))