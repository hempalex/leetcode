class Solution:
    def reverseVowels(self, s: str) -> str:

        indices = []
        l = list(s)

        for i, ch in enumerate(l):
            if ch in "aeiouAEIOU":
                indices.append(i)

        for i, pos in enumerate(indices):
            l[pos] = s[indices[-(i+1)]]

        return "".join(l)