class Solution:
    def canPartition(self, nums):

        total = sum(nums)
        # equal partition check
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[target]: return True
                dp[i] = dp[i] or dp[i - num]
        return dp[target]


if __name__ == '__main__':

    f = Solution()
    print(f.canPartition([1,5,11,5]))