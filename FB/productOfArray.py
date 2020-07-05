class Solution:
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

if __name__ == '__main__':
    f = Solution()
    i = [1, 2, 3, 4]
    print(f.productExceptSelf(i))