# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        first = prev = ListNode(None, head)

        while head and head.next:

            nn = head.next
            prev.next = nn
            head.next = nn.next

            if nn is not None:
                nn.next = head

            prev = head
            head = head.next

        return first.next

