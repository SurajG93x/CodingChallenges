import math

class Solution:
    def numSquares(self, n):
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            next = set()

            for n in queue:
                for num in square_nums:
                    if n == num:
                        return level
                    elif n < num:
                        break
                    else:
                        next.add(n - num)
            queue = next
        return level


if __name__ == '__main__':
    f = Solution()
    print(f.numSquares(12))