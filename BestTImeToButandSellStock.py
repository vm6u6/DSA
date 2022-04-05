def maxprofit( prices ):
    L = len(prices)
    ans = 0; Min = 10**4
    for i in range( L ):
        if prices[i] < Min:
            Min = prices[i]
        if prices[i] > Min:
            ans = max( ans, prices[i]-Min )
    return ans

# prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
# prices = [1,2]
prices = [2,4,1]
print ( maxprofit(prices) )