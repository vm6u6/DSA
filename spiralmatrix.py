def spiralmatrix( matrix ):
        if len(matrix) == 0:
            return []
        ans = []
        direct = 0 # 0 for right, 1 for down, 2 for left, 3 for up
        up = left = 0
        down,right = len(matrix) - 1,len(matrix[0]) - 1
        L = len(matrix)*len(matrix[0])
        while len(ans) < L:

            if direct == 0:
                for i in range(left,right + 1):
                    ans.append(matrix[up][i])
                up += 1
            elif direct == 1:
                for i in range(up,down + 1):
                    ans.append(matrix[i][right])
                right -= 1
            elif direct == 2:
                for i in range(left,right + 1)[::-1]:
                    ans.append(matrix[down][i])
                down -= 1
            else:
                for i in range(up,down + 1)[::-1]:
                    ans.append(matrix[i][left])
                left += 1
            direct = (direct + 1) % 4

        return ans

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralmatrix(matrix))