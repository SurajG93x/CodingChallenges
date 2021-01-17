class Solution:
    def test(self, s):
        if not s:
            return 0

        arr = [1]*len(s)

        for i in range(1,len(s)):
            for j in range(i):
                if s[i]>s[j]:
                    arr[i] = max(arr[i], arr[j]+1)

        return max(arr)


if __name__ == '__main__':
    f = Solution()
    print(f.test([1,4,0,3,4,5,2,6]))