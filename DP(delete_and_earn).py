def sum_same( tmp ):
    val = []
    idx = []
    cnt = 0
    tmp = sorted(tmp)
    for i in range( len(tmp) ):
        if (cnt == 0):
            cnt = tmp[i]

        if (i == (len(tmp)-1)):
            val.append(cnt)
            idx.append(tmp[i])
            return val, idx
        
        if ( tmp[i] == tmp[i+1] ):
            cnt = cnt + tmp[i]
        else:
            val.append(cnt)
            idx.append(tmp[i])
            cnt = 0

# greedy
def deleteandearn( nums ):
    L = len(nums)
    if L == 0:
        return 0    
    val, idx = sum_same(nums)
    big = max(idx)
    tmp = [0] * big
    for i in range(len(idx)):
        tmp[idx[i]-1] = val[i]

    Max = 0
    pre_max = 0
    pre_v = 0
    for i in range( len(tmp) ):
        Max = max( tmp[i]+pre_v, pre_max )
        pre_max, pre_v = Max, pre_max
    return Max

    # Max = 0
    # pre_max = 0
    # pre_v = 0
    # i = 0
    # while i < len(idx):
    #     print("Max: ", Max)
    #     print('pre: ', pre_v)
    #     print(i)
    #     if ( i+1<len(idx) ) and ( idx[i] != idx[i+1]-1 ):
    #         print("Here1")
    #         pre_v = pre_max + val[i+1]
    #         if ( i+2< len(idx) ):
    #             i = i + 2
    #         if ( i == 0 ):
    #             Max = val[i]
    #         else:
    #             Max = pre_max + val[i]
    #         pre_max = Max
    #     elif ( i == len(idx)-1 ):
    #         if ( idx[i] != idx[i-1]+1 ):
    #             Max = pre_max + val[i]
    #         else:
    #             Max = max( val[i]+pre_v, pre_max )
    #     else:
    #         print("Here2")
    #         Max = max( val[i]+pre_v, pre_max )
    #         pre_max, pre_v = Max, pre_max
    #     i = i + 1   
    #return Max

nums = [3,4,2]
print(deleteandearn( nums ))
