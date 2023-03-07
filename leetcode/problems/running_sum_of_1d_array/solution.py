class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        res = []
        for x in nums:
            sum += x
            res.append(sum)
        return res
            