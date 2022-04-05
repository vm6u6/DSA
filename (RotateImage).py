

# def rotate( matrix ):
#     row = len(matrix)
#     col = len(matrix[0])
#     tmp = {'ori':[], 'new':[], 'val':[]}
    
#     for i in range( row-1, -1, -1 ):
#         for j in range(col):
            
#             if ( [i, j] in tmp['ori'] ):
#                 print('Here2')
#                 idx = tmp['ori'].index([i,j])
#                 num = tmp['val'][idx]
#                 num2 = matrix[j][row-1-i]
#                 matrix[j][row-1-i] = num
#                 matrix[ tmp['new'][idx][0] ][ tmp['new'][idx][1] ] = num2
           
#             else:
#                 tmp['val'].append( matrix[j][row-1-i] )
#                 tmp['ori'].append( [j, row-1-i] )
#                 tmp['new'].append( [i, j] )
#                 num = matrix[j][row-1-i]
#                 matrix[j][row-1-i] = matrix[i][j] 
#                 matrix[i][j] = num
            
#             print(matrix)
                
def rotate( matrix):
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in range(rows // 2):
                for j in range(cols):
                    matrix[i][j], matrix[rows - i - 1][j] = matrix[rows - i - 1][j], matrix[i][j]
            for i in range(rows):
                for j in range(i):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1]]
# matrix = [[1,2],[3,4]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rotate(matrix)
print(matrix)