# %%
from typing import List

"""
Note: Python lists are always passed by reference !!!
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, x, y):
        grid[x][y] = '0'
        if x > 0 and grid[x - 1][y] == '1':
            self.bfs(grid, x - 1, y)
        if x < len(grid) - 1 and grid[x + 1][y] == '1':
            self.bfs(grid, x + 1, y)
        if y > 0 and grid[x][y - 1] == '1':
            self.bfs(grid, x, y - 1)
        if y < len(grid[0]) - 1 and grid[x][y + 1] == '1':
            self.bfs(grid, x, y + 1)
