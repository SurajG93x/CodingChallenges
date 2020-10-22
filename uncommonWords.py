'''
884. Uncommon Words from Two Sentences
Easy

437

86

Add to List

Share
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.
'''

from collections import Counter

class Solution:
    def uncommonFromSentences(self, A, B):
        cList = A.split() + B.split()
        count = Counter(cList)
        res = []
        for v,i in enumerate(count):
            if count[i] == 1:
                res.append(i)

        return res

if __name__ == '__main__':
    f = Solution()
    A = "this apple is sweet"
    B = "this apple is sour"
    print(f.uncommonFromSentences(A, B))
