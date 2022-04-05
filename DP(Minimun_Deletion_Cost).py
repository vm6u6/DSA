# def mincost( s, cost ):
#     L = len(s)
#     Min = 0
#     for i in range( 1, L ):
#         print(i)
#         if ( s[i] == s[i-1] ):
#             tmp = min( cost[i], cost[i-1] )
#             Min = tmp + Min
#             print("tmp: ", tmp)
#             print("Min: ", Min)
#     return Min

def mincost ( s, cost ):
    L = len(s)
    Min = 0
    n = 0
    m = 1
    while m < L:
        if ( s[n] == s[m] ):
            if ( cost[n] > cost[m] ):
                tmp = cost[m]
                n = n 
            else:
                tmp = cost[n]
                n = m
            Min = tmp + Min
            m = m + 1
        else:
            m = m + 1
            n = m - 1
    return Min

# s = "aaabbbabbbb"
# cost = [3,5,10,7,5,3,5,5,4,8,1]
s = "aaaaaaaaaaaaaa"
cost = [1,3,6,5,4,5,4,4,2,8,3,10,6,6]
print(mincost( s, cost ))