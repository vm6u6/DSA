

def dfs( grid, i ,j ):
    L = len(grid)
    L2 = len( grid[0] )
    if ( i<0 ) or ( j<0 ) or ( i>=L ) or ( j>=L2 ):
        return
    if ( grid[i][j] ) != "1":
        return 

    grid[i][j] = "0"
    dfs( grid, i-1 ,j )
    dfs( grid, i+1 ,j )
    dfs( grid, i ,j-1 )
    dfs( grid, i ,j+1 )

def traversal( grid ):
    L = len(grid)
    L2 = len( grid[0] )
    ans = 0
    for i in range( L ):
        for j in range( L2 ):
            if ( grid[i][j] == "1" ):
                ans = ans + 1
                dfs( grid, i, j )        
    return ans

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(traversal( grid ))
