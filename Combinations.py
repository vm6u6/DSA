def backtrack( n, k, tmp, ans, idx ):
    print("--start--")
    if len(tmp) == k:
        ans.append(tmp)
        return 
            
    for i in range (idx, n):
        print(tmp + [i+1])

        backtrack( n, k, tmp+[i+1], ans, i+1 )
        
            
n = 4; k = 2            
tmp = []; ans = []; idx = 0     
backtrack( n, k, tmp, ans, idx )
print(ans)