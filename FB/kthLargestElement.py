class Solution:
    def findKthLargest(self, nums, k):
        sortednums = sorted(nums)
        iternum = 0

        for i in range(len(sortednums)-1, -1, -1):
            iternum += 1
            if iternum == k:
                return sortednums[i]


if __name__ == '__main__':
    f = Solution()
    print(f.findKthLargest([3,2,1,5,6,4], 2))