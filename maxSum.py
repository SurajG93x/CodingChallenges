class Solution:
    def maxSubArray(self, nums):
        maxsum = nums[0]
        current = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            current = max(nums[i], current + nums[i])
            maxsum = max(maxsum, current)

        return maxsum

if __name__ == '__main__':
    f = Solution()
    print(f.maxSubArray([1,2]))