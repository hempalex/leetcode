class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        freq = defaultdict(int)
        
        for w in words:
            freq[w]+=1

        s = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        res = list(map(lambda x: x[0], s[:k]))

        return res
