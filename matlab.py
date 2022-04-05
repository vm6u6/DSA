x = [0.5, 0.3, -0.4, -0.2, 0.2, 0.3, -0.2, -0.5]
r0 = 0

for i in range( 8 ):
    r0 = r0 + x[i]*x[i]
print(r0)

r1 = 0
for i in range( 7 ):
    r1 = r1 + x[i]*x[i+1]
print(r1)

r1 = 0
for i in range( 6 ):
    r1 = r1 + x[i]*x[i+2]
print(r1)