class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid > 0 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[left] <= nums[mid] and nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1;

        return nums[left]

