class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(list(filter(None, map(lambda x: x.strip(), s.split(" "))))))
        

