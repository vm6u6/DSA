def mineatingspeed( piles, h ):

    L = len(piles)
    piles = sorted(piles)

    if h <= L:
        return piles[-1]
    
    

piles = [ 3, 6, 7, 11] ; h = 8
print(mineatingspeed(piles, h))