class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for ch in s:
            s_map[ch]+=1

        for ch in t:
            t_map[ch]+=1

        return t_map == s_map