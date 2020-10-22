class Solution:
    def hammingDistance(self, x, y):
        bx, by = "{0:b}".format(x), "{0:b}".format(y)
        n = max(len(bx), len(by))
        zx, zy = bx.zfill(n), by.zfill(n)
        count = 0

        for i in range(0, len(zx)):
            if zx[i] != zy[i]:
                count += 1

        return count

if __name__ == '__main__':
    f = Solution()
    print(f.hammingDistance(0, 41))