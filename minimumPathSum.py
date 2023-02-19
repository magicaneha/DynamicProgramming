'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

def minimum(grid):
    Rows,Cols=len(grid),len(grid[0])
    res=[[float("inf")] * (Cols + 1) for r in range(Rows + 1)]
    res[Rows-1][Cols]=0
    for r in range(Rows-1,-1,-1):
        for c in range(Cols-1,-1,-1):
            res[r][c]=grid[r][c]+ min (res[r+1][c],res[r][c+1])
    return res[0][0]



grid=[[1,3,1],[1,5,1],[4,2,1]]
print(minimum(grid))