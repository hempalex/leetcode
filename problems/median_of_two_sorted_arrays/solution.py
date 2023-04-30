class Solution:
    def mergeTwoAscendingLists(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res = []

        n1 = iter(nums1)
        n2 = iter(nums2)

        x1 = next(n1, None)
        x2 = next(n2, None)

        while True:

            if x1 == None or x2 == None:

                if x1 != None:
                    res.append(x1)
                if x2  != None:
                    res.append(x2)

                break

            if x1 < x2:
                res.append(x1)
                x1 = next(n1, None)
            else:
                res.append(x2)
                x2 = next(n2, None)


        x1 = next(n1, None)
        while x1 != None:
            res.append(x1)
            x1 = next(n1, None)

        x2 = next(n2, None)
        while x2 != None:
            res.append(x2)
            x2 = next(n2, None)

        return res


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = self.mergeTwoAscendingLists(nums1, nums2)

        length = len(nums)
        index = (length - 1) // 2

        if (length % 2):
            return nums[index]
        else:
            return (nums[index] + nums[index + 1])/2.0