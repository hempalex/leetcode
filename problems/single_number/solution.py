class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        n = nums[0]

        for x in nums[1:]:
            n ^= x

        return n
            