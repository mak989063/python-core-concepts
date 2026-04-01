"""
grid = [
  ["1","1","0"],
  ["1","0","0"],
  ["0","1","1"]
]
"1" = land
"0" = water

How many separate islands?
"""

def numIslands(grid):
    m, n = len(grid), len(grid[0])

    def dfs(i, j):
        # boundary + water check
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
            return

        # mark visited
        grid[i][j] = "0"

        # explore all directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs(i, j)   # explore whole island
                count += 1

    return count

grid = [
  ["1","1","0"],
  ["1","0","0"],
  ["0","1","1"]
]

print(numIslands(grid))