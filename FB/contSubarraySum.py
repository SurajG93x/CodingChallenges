class Solution:
    def checkSubarraySum(self, nums, k):
        # sum = 0
        # map = {}
        # map[0] = -1
        # for i in range(0, len(nums)):
        #     sum += nums[i]
        #     if k != 0:
        #         sum = sum % k
        #     if sum in map:
        #         if i - map[sum] > 1:
        #             return True
        #     else:
        #         map[sum] = i
        # return False
        n = len(nums)
        for i in range(0, n):
            total = 0
            minsum = 0
            for j in range(i,n):
                if total > k:
                    break
                total += nums[j]
                minsum += 1
                if k == 0:
                    if minsum >= 2 and total == 0:
                        return True
                else:
                    if total % k == 0 and minsum >=2:
                        return True
        return False


if __name__ == '__main__':
    f = Solution()
    ar = [1,2,3,2]
    k = 4
    print(f.checkSubarraySum(ar, k))