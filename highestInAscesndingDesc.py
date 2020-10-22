'''
3. Suppose an array of integers are arranged from lowest to highest, then back to
lowest again. Implement an efficient C++ function that finds the index for the highest
number in the sequence. For example [1, 4, 8, 9 , 7, 1, -2, -5, -7] would return ‘3’ since 9
is in the peak. [1,10,50,10,1] would return ‘2’ since 50 is the peak. If the input is invalid
(including multiple consecutive peak numbers), return -1.
'''

from setuptools import setup
from Cython.Build import cythonize

class Solution:
    def getHighest(self, nums):
        if not nums:
            return -1
        elif len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] < nums[mid-1]:
                right-=1
            elif nums[mid] < nums[mid+1]:
                left+=1
            elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            else: return -1


if __name__ == '__main__':
    f = Solution()
    print(f.getHighest([1, 4, 8, 9 , 7, 1, -2, -5, -7]))

setup(
        name='Hello world app',
        ext_modules=cythonize("highestInAscesndingDesc.py"),
        zip_safe=False,
    )