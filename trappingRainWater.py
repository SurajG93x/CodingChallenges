'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        leftmax = [0] * n
        rightmax = [0] * n
        res = 0

        leftmax[0] = height[0]
        rightmax[-1] = height[-1]

        for i in range(1, n):
            leftmax[i] = max(height[i], leftmax[i - 1])
        for j in range(n - 2, -1, -1):
            rightmax[j] = max(height[j], rightmax[j + 1])
        for x in range(1, n):
            res += min(leftmax[x], rightmax[x]) - height[x]

        return res

if __name__ == '__main__':
    f = Solution()
    print(f.trap([0,1,0,2,1,0,1,3,2,1,2,1]))