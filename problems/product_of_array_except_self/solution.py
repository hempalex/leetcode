class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        res = [1] * len(nums)

        product = 1
        for i in range(1, len(nums)):
            product *= nums[i - 1]
            res[i] = product

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]
        
        return res