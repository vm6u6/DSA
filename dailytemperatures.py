# TLE
def dailytemperatures ( tmpera ):
    L = len(tmpera)
    ans = [0] * L

    p1 = 0
    while ( p1 < L-1 ):
        if tmpera[p1] < tmpera[p1+1]:
            ans[p1] = 1
        else:
            for i in range( p1, L ):
                if tmpera[i] > tmpera[p1]:
                    ans[p1] = i - p1
                    break
        p1 = p1 + 1
    return ans

def dailytemperatures ( t ):
    L = len(t)
    tmp = []
    for i in range( L ):
        
        

temper = [73,74,75,71,69,72,76,73]
temper = [30,60,90,60]
print( dailytemperatures(temper) )