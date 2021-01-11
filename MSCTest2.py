class Solution:
    def test(self, message, k):
        words = message.split(" ")
        res = []

        for word in words:
            n = len(word)
            if n <= k:
                res.append(word)
                k -= n + 1
            else:
                break

        return " ".join(res)


if __name__ == '__main__':
    f = Solution()
    print(f.test('The quick brown fox jumps over the lazy dog', 39))