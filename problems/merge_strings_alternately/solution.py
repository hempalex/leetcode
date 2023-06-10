class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        w1, w2 = 0, 0

        res = []

        while w1 < len(word1) or w2 < len(word2):
            if w1 < len(word1):
                res.append(word1[w1])
                w1 += 1

            if w2 < len(word2):
                res.append(word2[w2])
                w2 += 1

        return "".join(res)

