'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums):
        neg = {}
        pos = {}
        zeros = 0
        solutions = set()

        for i in nums:
            if i < 0:
                neg.setdefault(i, 0)
                neg[i] += 1
            elif i > 0:
                pos.setdefault(i, 0)
                pos[i] += 1
            else:
                zeros += 1

        for i in {num for num in nums}:
            if i < 0:
                for j in pos:
                    k = -i - j
                    if k in pos:
                        if k == j and pos[j]-1 < 1:
                            continue
                        else:
                            solutions.add(tuple(sorted((i, j, k))))
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            elif i > 0:
                for j in neg:
                    k = -i - j
                    if k in neg:
                        if k == j and neg[j]-1 < 1:
                            continue
                        else:
                            solutions.add(tuple(sorted((i, j, k))))
                    elif k == 0 and zeros > 0:
                        solutions.add(tuple(sorted((i, j, 0))))

            elif zeros >= 3:
                solutions.add((0, 0, 0))

        return [list(s) for s in solutions]

if __name__ == '__main__':
    f = Solution()
    print(f.threeSum([-1, 0, 1, 2, -1, -4]))