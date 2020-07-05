class Solution:
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True

if __name__ == '__main__':
    f = Solution()
    a = [2, 3, 1, 1, 4]
    b = [3, 2, 1, 0, 4]
    print(f.canJump(b))
