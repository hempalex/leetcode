class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cache = {}

        for index, value in enumerate(nums):

            required = target - value

            if required in cache:
                return [cache[required], index]
            else:
                cache[value] = index
