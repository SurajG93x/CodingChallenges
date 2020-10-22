'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''


class Solution:
    def majorityElement(self, nums):
        res = []
        if not nums:
            return res

        n1 = None
        n2 = None
        c1 = 0
        c2 = 0

        for n in nums:
            if n == n1:
                c1 += 1
            elif n == n2:
                c2 += 1
            elif c1 == 0:
                n1 = n
                c1 += 1
            elif c2 == 0:
                n2 = n
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        for n in [n1, n2]:
            if nums.count(n) > len(nums) / 3:
                res.append(n)

        return res

if __name__ == '__main__':
    f = Solution()
    print(f.majorityElement([1,1,1,3,3,2,2,2]))