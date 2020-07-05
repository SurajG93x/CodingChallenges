class Solution:
    def isAlienSorted(self, words, order):
        alpha_list = {letter: i for i, letter in enumerate(order)}

        for x in range(0, len(words)-1):
            word1 = words[x]
            word2 = words[x+1]

            for i in range(0,min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    if alpha_list[word1[i]] > alpha_list[word2[i]]:
                        return False
                elif len(word1) > len(word2):
                    return False
        return True


if __name__ == '__main__':
    f = Solution()
    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(f.isAlienSorted(words,order))