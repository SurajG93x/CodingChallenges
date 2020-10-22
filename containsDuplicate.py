class Solution:
    def containsNearbyDuplicate(self, nums, k):
        iDict = {}

        for i, val in enumerate(nums):
            if val in iDict and i - iDict[val] <= k:
                return True
            iDict[val] = i

        return False

if __name__ == '__main__':
    f = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    print(f.containsNearbyDuplicate(nums, k))