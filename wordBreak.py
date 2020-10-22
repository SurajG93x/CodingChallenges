'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''


class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [False] * (len(s)+1)
        dp[0] = True

        for start in range(len(s)):
            for end in range(start,len(s)):
                if dp[start] and s[start:end+1] in wordDict:
                    dp[end+1] = True

        return dp[-1]

if __name__ == '__main__':
    f = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(f.wordBreak(s,wordDict))