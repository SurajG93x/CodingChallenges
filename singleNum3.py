'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''

from collections import Counter

class Solution:
    def singleNumber(self, nums):
        count = Counter(nums).most_common()
        return [count[-1][0],count[-2][0]]


if __name__ == '__main__':
    f = Solution()
    print(f.singleNumber([1,2,1,3,2,5]))
