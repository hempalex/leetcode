class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left, right = 0, len(nums) - 1
        while left <= right:

            while left < right and nums[left] == nums[left + 1]:
                left = left + 1

            while right > left and nums[right] == nums[right - 1]:
                right = right - 1

            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[mid] > nums[right]:
                if  nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if  nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

