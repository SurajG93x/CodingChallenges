class Solution:
    def nextGreaterElements(self, nums):
        ln = len(nums)
        if ln == 0:
            return []
        stack = []
        res = [-1] * ln
        # Run it twice. After first iteration
        # the stack has the increasing order of elements from starting
        # so in second iteration you will get the next greater from stack
        # which was on the left side of that node
        for _ in range(2):
            for i in range(ln - 1, -1, -1):
                while len(stack) > 0 and stack[-1] <= nums[i]:
                    stack.pop()
                if len(stack) > 0:
                    res[i] = stack[-1]

                stack.append(nums[i])

        return res


if __name__ == '__main__':
    f = Solution()
    print(f.nextGreaterElements([1,2,7,3,4,5,1]))