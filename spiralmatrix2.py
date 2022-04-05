def generatespiral ( n ):

    ans = []; tmp = []
    for i in range(n):
        for j in range(n):
            tmp.append(0)
        ans.append(tmp)
        tmp = []

    up = 0; down = n-1; right = n-1; left = 0
    direct = 0; cnt = 1

    while up <= down and left <= right:

            if direct == 0:
                for i in range(left,right + 1):
                    ans[up][i] = cnt
                    cnt = cnt + 1
                up += 1
            elif direct == 1:
                for i in range(up,down + 1):
                    ans[i][right] = cnt 
                    cnt = cnt + 1
                right -= 1
            elif direct == 2:
                for i in range(left,right + 1)[::-1]:
                    ans[down][i] = cnt 
                    cnt = cnt + 1
                down -= 1
            else:
                for i in range(up,down + 1)[::-1]:
                    ans[i][left] = cnt 
                    cnt = cnt + 1
                left += 1
            direct = (direct + 1) % 4

    return ans

n = 3
print(generatespiral(n))