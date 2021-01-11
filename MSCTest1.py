class Solution:
    def twoSum(self, number):
        sibling = int("".join(sorted([i for i in str(number)],reverse=True)))
        if sibling > 100000000:
            return -1
        return sibling

if __name__ == '__main__':
    f = Solution()
    print(f.twoSum(213))