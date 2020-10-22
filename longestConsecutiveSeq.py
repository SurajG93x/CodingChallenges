'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''


class Solution:
    def longestConsecutive(self, nums):
        longest = 0

        numSet = set(nums)

        for n in numSet:
            if n-1 not in numSet:
                curr = n
                count = 1

                while curr + 1 in numSet:
                    curr += 1
                    count += 1

                longest = max(longest,count)

        return longest

if __name__ == '__main__':
    f = Solution()
    print(f.longestConsecutive([100, 4, 200, 1, 3, 2]))