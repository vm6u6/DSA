
def ninenine( num1, num2, ans ):
    num2 = num2 + 1
    if ( num2 > 9 ):
        num1 = num1 + 1
        num2 = 0
        print( ans )
        ans = []
    else:
        val = num1 * num2
        ans.append( val )
        
    if ( num1 < 10 ):
        ninenine(num1, num2, ans)
    else:
        print("Finish")

num1 = 1
num2 = 0
ans = []
ninenine(num1, num2, ans)