'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        rows = len(image)
        cols = len(image[0])
        color = image[sr][sc]

        if color == newColor:
            return image

        def dfs(row,col):
            if image[row][col] == color:
                image[row][col] = newColor

                if row >= 1: dfs(row-1,col)
                if row+1 < rows: dfs(row+1,col)
                if col >= 1: dfs(row,col-1)
                if col+1 < cols: dfs(row,col+1)

        dfs(sr,sc)
        return image


if __name__ == '__main__':
    f = Solution()
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print(f.floodFill([[0,0,0],[0,1,1]],1,1,1))
