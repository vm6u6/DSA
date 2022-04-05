# Given n non-negative integers representing an elevation map where the width of each bar is 1
# compute how much water it can trap after raining.

def trap( h ):
    L = len(h)
    n, m = 0, 1
    Max = 0; Max2 = 0; water = 0 
    small = []
    preMax = []
    while ( m < L ):
        print( "iteration start" )
        print( "h[n]: ", h[n] )
        print( "h[m]: ", h[m] )
        if ( h[n] > h[m] ):
            Max = h[n]
            if ( m > n + 1 ) and ( h[m] > h[m-1] ):
                Max2 = h[m]
            small.append( h[m] )
            print( "small: ", small )
            if ( Max2 > 0 ) and ( Max > 0 ) and ( m<L-1 ):
                preMax.append( Max2 )
                for i in range( len(small) ):
                    water = water + Max2 - small[i]
            n = n
            m = m + 1
        elif ( h[m] > h[n] ):
            Max = h[m]
            Max2 = h[n]
            print( "small: ", small )
            preMax.append( Max2 )
            for i in range( len(small) ):
                    water = Max2 - small[i] + water
            Max2 = 0
            small = []
            n = m
            m = m + 1
        else:
            n = n + 1
            m = m + 1
        print("Max1: ", Max)
        print("Max2: ", Max2)
        print("preMax: ", preMax )
        print("water: ", water)
    return water


#height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print( trap( height ) )

