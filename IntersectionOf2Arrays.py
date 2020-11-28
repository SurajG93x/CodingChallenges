class Solution:
    def intersection(self, nums1,nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)

        ans = []

        if len(nums2) > len(nums1):
            s1 = nums1
            s2 = nums2
        else:
            s1, s2 = nums2, nums1

        for x in len(s1):
            if x in s2:
                ans.append(x)

        return ans

if __name__ == '__main__':
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    f = Solution()
    print(f.intersection(nums1,nums2))