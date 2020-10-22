'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            pal = self.palindrome(s, i, i)
            if len(pal) > len(res):
                res = pal
            pal = self.palindrome(s, i, i + 1)
            if len(pal) > len(res):
                res = pal

        return res

    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

if __name__ == '__main__':
    f = Solution()
    print(f.longestPalindrome("babad"))