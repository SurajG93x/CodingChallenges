'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
'''

class Solution:
    def singleNumber(self, nums) -> int:
        return (3*sum(set(nums)) - sum(nums))//2


if __name__ == '__main__':
    f = Solution()
    print(f.singleNumber([0,1,0,1,0,1,99]))