'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''


class Solution:
    def countSmaller(self, nums):
        # dp = {}
        # n = len(nums)
        # dp[nums[n - 1]] = 1
        # res = []
        # res.append(0)
        #
        # for i in range(len(nums) - 2, -1, -1):
        #     c = 0
        #     for j in dp.keys():
        #         if nums[i] > j:                           #FUCKING TLE
        #             c+=dp[j]
        #     dp.setdefault(nums[i], 0)
        #     dp[nums[i]]+=1
        #
        #     res.append(c)
        #
        # res.reverse()
        # return res
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

if __name__ == '__main__':
    f = Solution()
    print(f.countSmaller([5,2,6,1]))