'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        sDict = Counter(s)
        res = 0
        odd = False

        for i in sDict:
            if sDict[i] % 2 == 0:
                res += sDict[i]
            else:
                res += sDict[i] - 1
                odd = True

        return res if odd is False else res +1

if __name__ == '__main__':
    f = Solution()
    print(f.longestPalindrome("abccccdd"))