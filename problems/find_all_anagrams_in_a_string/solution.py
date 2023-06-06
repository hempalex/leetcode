class Solution:
    def freqTable(self, s: str) -> dict[str, int]:

        d = {}
        for i in range(ord("a"), ord("z")+1):
            d[chr(i)] = 0

        for ch in s:
            d[ch] += 1

        return d


    def findAnagrams(self, s: str, p: str) -> List[int]:


        if len(p) > len(s):
            return []

        freq_p = self.freqTable(p)

        l = len(p)

        freq = self.freqTable(s[0:l])

        res = []


        if freq == freq_p:
            res.append(0)

        for i in range(1, len(s) - l + 1):
            remove = s[i-1]
            add = s[i+l-1]
            freq[remove] -= 1
            freq[add] += 1

            if freq == freq_p:
                res.append(i)

        return res
