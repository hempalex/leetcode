# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        first = res = ListNode(None)
        overflow = 0

        while l1 or l2:

            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next

            if l2:
                v2 = l2.val
                l2 = l2.next

            val = overflow + v1 + v2
            overflow = val // 10
            cur = val % 10

            res.next = ListNode(cur)
            res = res.next
        
        if overflow:
            res.next = ListNode(overflow)

        return first.next
