'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(set(nums1 + nums2))
        sum =0
        c=0
        for n in nums:
            sum += n
            c+=1

        return sum/c

if __name__ == '__main__':
    f = Solution()
    nums1 = [3]
    nums2 = [-2,-1]
    print(f.findMedianSortedArrays(nums1,nums2))