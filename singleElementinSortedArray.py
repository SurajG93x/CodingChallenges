'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Follow up: Your solution should run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''


class Solution:
    def singleNonDuplicate(self, nums):
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            evenHalf = False
            if (high - mid) % 2 == 0:
                evenHalf = True
            if nums[mid + 1] == nums[mid]:
                if evenHalf:
                    low = mid + 2
                else:
                    high = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if evenHalf:
                    high = mid - 2
                else:
                    low = mid + 1
            else:
                return nums[mid]
        return nums[low]

if __name__ == '__main__':
    f = Solution()
    print(f.singleNonDuplicate([1,1,2,3,3,4,4]))