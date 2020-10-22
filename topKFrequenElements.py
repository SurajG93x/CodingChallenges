from collections import  Counter

class Solution:
    def topKFrequent(self, nums, k):
        counts = list(Counter(nums).most_common(k))
        return [c[0] for c in counts]

if __name__ == '__main__':
    f = Solution()
    print(f.topKFrequent([3,0,1,0], 1))