'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charDict = {}

        for i in s:
            if i not in charDict:
                charDict[i] = 1
            else:
                charDict[i] += 1

        for j in t:
            if j not in charDict:
                return False
            else:
                charDict[j] -= 1

        for ch in charDict.values():
            if ch != 0: return False
        return True


if __name__ == '__main__':
    f = Solution()
    s = "anagram"
    t = "nagaram"
    print(f.isAnagram(s,t))