'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''

from  collections import deque

class Solution:
    def orangesRotting(self, grid):
        rotten = deque()
        freshSet = set()
        rows = len(grid)
        cols = len(grid[0])
        minutes = 0
        directions = [(1,0), (-1,0), (0,1),(0,-1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    rotten.append((i,j,minutes))
                elif grid[i][j] == 1:
                    freshSet.add((i,j))

        while rotten:
            curr = rotten.popleft()
            r = curr[0]
            c = curr[1]
            minutes = curr[2]

            for dir in directions:
                dx = dir[0]
                dy = dir[1]
                if 0<=r+dx<rows and 0<=c+dy<cols and grid[r+dx][c+dy] == 1:
                    grid[r + dx][c + dy] = 2
                    freshSet.remove((r + dx,c+dy))
                    rotten.append((r + dx,c+dy,minutes+1))

        if not freshSet: return minutes
        else: return -1

if __name__ == '__main__':
    f = Solution()
    print(f.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))