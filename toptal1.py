class Solution:
    def solution(self, S, K):
        def count(start, end, c, left):
            if left < 0:
                return float('inf')
            if start >= len(S): return 0
            if S[start] == end:
                i = 1 if c == 1 or c == 9 or c == 99 else 0
                return i + count(start+1, end, c+1, left)
            else:
                currcount = 1 + count(start+1, S[start], 1, left)
                prevcount = count(start+1, end, c, left-1)
                return min(currcount, prevcount)
        return count(0,"",0,K)


if __name__ == '__main__':
    f = Solution()
    print(f.solution("aaabcccd",2))