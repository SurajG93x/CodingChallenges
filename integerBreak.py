'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
'''


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [None, 1]

        for x in range(2, n+1):
            j = x-1
            i = 1
            maxpr = 0

            while i <= j:
                maxpr = max(maxpr, max(i,dp[i]) * max(j, dp[j]))
                i += 1
                j -= 1
            dp.append(maxpr)

        return dp[n]


if __name__ == '__main__':
    f = Solution()
    print(f.integerBreak(10))