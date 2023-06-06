class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        k = 1
        cnt = 1

        for i in range(1, len(nums)):

            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                cnt = 1
                k += 1


            elif cnt < 2:
                nums[k] = nums[i]
                cnt += 1
                k += 1

        return k
