
def merge( num1, m, num2, n ):
    if m == 0:
        num1 = []
    else: 
        num1 = num1[ :m ]
    if n == 0:
        num2 = []
    else: 
        num2 = num2[ :n ]
    i = 0
    j = 0
    sorted = []
    while ( i < m ) or ( j < n ):
        if i >= m:
            sorted.append( num2[j] )
            j = j + 1
        elif j >=n:
            sorted.append( num1[i] )
            i = i + 1
        elif num1[i] > num2[j]:
            sorted.append( num2[j] )
            j = j + 1
            print(j)
        else:
            sorted.append( num1[i] )
            i = i + 1
            print(i)


# nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
# merge( nums1, m, nums2, n )

# nums1 = [1]; m = 1; nums2 = []; n = 0
# merge( nums1, m, nums2, n )

nums1 = [0]; m = 0; nums2 = [1]; n = 1
merge( nums1, m, nums2, n )

# nums1 = [4,0,0,0,0,0]; m = 1; nums2 = [1,2,3,4,5,6]; n = 5
# merge( nums1, m, nums2, n )