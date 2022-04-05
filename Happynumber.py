def calHappy( n ):
    print(n)
    nums = str(n); ans = 0
    if n == 1:
        return True
    if n in tmp:
        return False
    tmp.append(n)
    for i in nums:
        ans = (int(i))**2 + ans 
        
    return calHappy( ans )

tmp = []           
n = 2 
print(calHappy( n ))
print(tmp)