'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        dp = defaultdict()

        for i, v in enumerate(nums):
            if target - v in dp:
                return [dp[target - v], i]
            else:
                dp[v] = i

if __name__ == '__main__':
    f = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(f.twoSum(nums,target))