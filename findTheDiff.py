class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = sorted(s)
        y = sorted(t)
        for i,j in enumerate(x):
            if j != y[i]: return y[i]
        return y[-1]

if __name__ == '__main__':
    f = Solution()
    print(f.findTheDifference("acfds","afrdcs"))
