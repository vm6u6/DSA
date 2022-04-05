def WordSearch( board, word ):

    def helper( board, word, tmp, idx  ):
        i = tmp[0]
        j = tmp[1]

        if idx == len(word):
            return True

        if board[i][j] != word[idx]:
            return
        else:
            idx = idx + 1

        

        
    col = len(board[0])  # 4
    row = len(board)     # 3
    tmp = []
    for i in range( row ):
        for j in range( col ):
            if board[i][j] == word[0]:
                tmp.append( [i, j] )
    
    for i in tmp:
        if helper( board, word, tmp[i], 0 ):
            return True
    return False
    
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
print(WordSearch( board, word ))
