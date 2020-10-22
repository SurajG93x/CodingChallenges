'''
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.



Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed.
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]


Constraints:

1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.
'''

class Solution:
    def printVertically(self, s):
        wordList = s.split()
        n = len(max(wordList, key=len))
        mat = []

        for word in wordList:
            ans = []
            for c in range(len(word)):
                ans.append(word[c])
            for _ in range(n - len(word)):
                ans.append(0)
            mat.append(ans)

        res = []

        rlen = len(mat[0])
        clen = len(mat)
        for i in range(rlen):
            wr = ""
            for j in range(clen):
                if mat[j][i] != 0:
                    wr += mat[j][i]
                else: wr += " "
            res.append(wr.rstrip())

        return res


if __name__ == '__main__':
    f = Solution()
    print(f.printVertically("TO BE OR NOT TO BE"))