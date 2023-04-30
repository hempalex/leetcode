class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        seen = {}
        general_max = m = 0

        for idx, ch in enumerate(s):

            if ch in seen:
                m = max(m, seen[ch] + 1);

            seen[ch] = idx
            general_max = max(general_max, idx - m + 1);

        return general_max

