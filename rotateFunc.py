from collections import deque

class Solution:
    def maxRotateFunction(self, A):
        s, n = sum(A), len(A)
        cur_sum = sum([i * j for i, j in enumerate(A)])
        ans = cur_sum
        for i in range(n): ans = max(ans, cur_sum:= cur_sum + s - A[n - 1 - i] * n)
        return ans


if __name__ == '__main__':
    f = Solution()
    print(f.maxRotateFunction([4, 3, 2, 6]))