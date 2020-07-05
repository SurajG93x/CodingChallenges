'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution:
    def numIslands(self, grid):
        if grid is None and len(grid) == 0:
            return 0

        cols = len(grid)
        rows = len(grid[0])
        islands = 0

        for col in range(0, cols):
            for row in range(0, rows):
                if grid[col][row] == '1':
                    islands += 1
                    self.dfs(grid, col, row)

        return islands

    def dfs(self, grid, c, r):
        cols = len(grid)
        rows = len(grid[0])

        if c < 0 or r < 0 or c >= cols or r >= rows or grid[c][r] == '0':
            return

        grid[c][r] = '0'
        self.dfs(grid, c + 1, r)
        self.dfs(grid, c - 1, r)
        self.dfs(grid, c, r + 1)
        self.dfs(grid, c, r - 1)



if __name__ == '__main__':
    f = Solution()
    print(f.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))