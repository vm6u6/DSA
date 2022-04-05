def fun1():
    x = 5
    def fun2( x ):
        x *= 2
        return x
    return fun2( x )

result = fun1()
print(result)
