'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        r = 0
        while n > 0:
            n //= 5
            r += n
        return r


if __name__ == '__main__':
    f = Solution()
    print(f.trailingZeroes(6508))