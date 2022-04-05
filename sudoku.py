def check_row( val ):
    seen = []
    for i in val:
        if i in seen and i != ".":
            return False
        else:
            seen.append(i)

def check_col ( board, idx ):
    val = []
    for i in board: 
        val.append( i[idx] )
    if check_row(val) is False:
        return False
    else:
        return True    

def check_suqare( board, idx ):
    tmp = []
    for i in range( 3 ):
        no1 = idx[0] + i
        for j in range( 3 ):
            no2 = idx[1] + j
            tmp.append( board[no1][no2] ) 
    if check_row(tmp) is False:
        return False
    else:
        return True

def valid_sudoku ( board ):
    L = len(board)
    # check row
    for i in range ( L ):
        if check_row( board[i] ) is False:
            return False
    
    # check col
    for i in range( L ):
        if check_col( board, i ) is False:
            return False

    # check square
    start_point = []
    for i in range( 0, 7, 3 ):
        for j in range( 0, 7, 3 ):  
            start_point.append( [i, j] ) 
    for i in start_point:
        if check_suqare(board, i) is False:
            return False
    return True  


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","1",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
print(valid_sudoku( board ))

# board = [["5","3",".",".","7",".",".",".","."]
#         ,["6",".",".","1","9","5",".",".","."]
#         ,[".","9","8",".",".",".",".","6","."]
#         ,["8",".",".",".","6",".",".",".","3"]
#         ,["4",".",".","8",".","3",".",".","1"]
#         ,["7",".",".",".","2",".",".",".","6"]
#         ,[".","6",".",".",".",".","2","8","."]
#         ,[".",".",".","4","1","9",".",".","5"]
#         ,[".",".",".",".","8",".",".","7","9"]]
# print(valid_sudoku( board ))