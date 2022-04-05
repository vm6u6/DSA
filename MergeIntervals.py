def merge( intervals ):
    L = len(intervals)
    arr = sorted(intervals, key = lambda x: x[0])
    tmp = arr[0]; res = []

    for i in range( 1, L ):
        if tmp[0] <= arr[i][0] <= tmp[1]:
            tmp = [ tmp[0], max( arr[i][1], tmp[1] ) ]
        else:
            res.append( tmp )
            tmp = arr[i]
    res.append(tmp)
    return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
print( merge( intervals ) )