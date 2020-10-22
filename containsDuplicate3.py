'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for i, v1 in enumerate(nums):
            for j in range(i+1,i+k+1):
                if j >= len(nums):
                    break
                v2 = nums[j]
                if abs(v1 - v2) <= t:
                    return True

        return False

if __name__ == '__main__':
    f = Solution()
    print(f.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))