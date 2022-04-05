def modify ( s, tmp, i, L, spec ):
    print( "S:",s )
    if i >= spec:
        print( "i:", i )
        
        return s
    
    tmp = s[i]
    s[i] = s[L-1]
    s[L-1] = tmp
    modify( s, tmp, i+1, L-1, spec )
            

s = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ",
     "a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]           
L = len(s)
spec = L//2
print(spec)
tmp = 0
i = 0
modify ( s, tmp, i, L, spec )
print(s)