
output = []
def recur_diff( input ):

    res = []
    N = len(input)
    
    print(input)
    for i in range(N):
        print( "--START--" )
        if input[i] == "+" or input[i] == "-" or input[i] == "*":
            print("Left~~")
            lefts = recur_diff(input[:i])
            print("Right~~")
            rights = recur_diff(input[i+1:])
            print( "Left:", lefts )
            print( "Right:", rights )
            for left in lefts:
                for right in rights:
                    if input[i] == "+":
                        res.append(left + right)
                    elif input[i] == "-":
                        res.append(left - right)
                    elif input[i] == "*":
                        res.append(left * right)
            print( "res:", res )
        
    if not res:
        res.append(int(input))
    return res


s = "2+1-1"
print(recur_diff( s ))
print(output)
