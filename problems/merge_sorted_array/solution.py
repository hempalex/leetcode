class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            return

        for i in range(m+n-1, -1, -1):
            if m > 0 and n == 0:
                m -= 1
                nums1[i] = nums1[m]

            if m == 0 and n > 0:
                n -= 1
                nums1[i] = nums2[n]

            if m > 0 and n > 0:
                if nums1[m-1] > nums2[n-1]:
                    m -= 1
                    nums1[i] = nums1[m]
                else:
                    n -= 1
                    nums1[i] = nums2[n]