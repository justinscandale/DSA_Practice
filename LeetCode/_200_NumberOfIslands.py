#  LINK TO PROBLEM:
#  https://leetcode.com/problems/number-of-islands/description/

#  TAGS:
#  GRAPHS, DFS

#  SOLUTION:
# This problem will be solved using dfs.  We will start at row 0, then we will check if the value at that position is a 1.
# If it is we will call our dfs function on that position, increment the isalnd count by 1, and set the value at that position to 0.
# We then will call the dfs function for the position above, below, to the left, and to the right of the current position.
# We continue this process until all positions in grid are checked

# TIME COMPLEXITY:  O(n*m) - where n is the number of rows and m is the number of columns
# SPACE COMPLEXITY:  O(n*m) - for the recursive call stack

import copy

def numIslands(grid: list[list[str]]) -> int:

    def dfs(row,col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == '0':
            return
        else:
            grid[row][col] = '0'
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
    
    islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1':
                islands += 1
                dfs(row,col)
    
    return islands

def numIslands2(grid: list[list[str]]) -> int:

    def bfs(row,col):
        queue = [(row,col)]

        while queue:
            row,col = queue.pop(0)
            if row+1 < len(grid) and grid[row+1][col] == '1':
                queue.append((row+1,col))
                grid[row+1][col] = '0'
            if row-1 >= 0 and grid[row-1][col] == '1':
                queue.append((row-1,col))
                grid[row-1][col] = '0'
            if col+1 < len(grid[row]) and grid[row][col+1] == '1':
                queue.append((row,col+1))
                grid[row][col+1] = '0'
            if col-1 >= 0 and grid[row][col-1] == '1':
                queue.append((row,col-1))
                grid[row][col-1] = '0'
            
    islands = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1':
                islands += 1
                bfs(row,col)

    return islands

# Testing code
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(copy.deepcopy(grid)))
print(numIslands2(copy.deepcopy(grid)))