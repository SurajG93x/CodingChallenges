'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
'''


class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    val = 0
                    if i != 0: val += grid[i-1][j]
                    if j != 0: val += grid[i][j-1]
                    if i != rows-1: val += grid[i+1][j]
                    if j != cols-1: val += grid[i][j+1]
                    res += 4 - val

        return res

if __name__ == '__main__':
    f = Solution()
    print(f.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))