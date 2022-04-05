
def departString( s ):
    L = len(s)
    num = ''
    all = []
    for i in range( L ):
        if ( s[i] == "+" ):
            all.append( int(num) )
            all.append("+")
            num = ''
        elif ( s[i] == "-" ):
            all.append( int(num) )
            all.append("-")
            num = ''
        elif ( s[i] == "*" ):
            all.append( int(num) )
            all.append("*")
            num = ''
        elif ( s[i] == "/" ):
            all.append( int(num) )
            all.append("/")
            num = ''
        else:
            num = num + s[i]
            if ( i == L-1 ):
                all.append(int(num))
    return all

def MD( all ):
    L = len(all)
    i = 0
    tmp = 0 
    while i < L - 1: 
        if ( all[i] == '*' ) or ( all[i] == '/' ):
            if ( all[i] == '*' ):
                tmp = all[i-1] * all[i+1]
            else:
                tmp = all[i-1] // all[i+1]
            all.pop(i)
            all.pop(i)
            all.pop(i-1)
            all.insert(i-1,tmp)
            L = L - 2
        else:
            i = i + 1
    return all

def PM( all ):
    L = len(all)
    i = 0
    tmp = 0 
    while i < L - 1: 
        if ( all[i] == '+' ) or ( all[i] == '-' ):
            if ( all[i] == '+' ):
                tmp = all[i-1] + all[i+1]
            else:
                tmp = all[i-1] - all[i+1]
            all.pop(i)
            all.pop(i)
            all.pop(i-1)
            all.insert(i-1,tmp)
            L = L - 2
        else:
            i = i + 1
    return all

def calculator ( s ):
    all = PM(MD(departString(s)))
    return all[0]
    
s = "2*3+56"
print( calculator(s) )

