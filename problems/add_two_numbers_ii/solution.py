# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            previous = None
            current = head
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
            return previous

        l1 = reverseList(l1)
        l2 = reverseList(l2)

        overflow = 0
        head = res = ListNode(0)

        while l1 or l2 or overflow:
            
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val

            val = v1 + v2 + overflow

            #print(f"v1={v1} v2={v2} overflow={overflow} val={val}")

            res.val = val % 10
            overflow = val // 10

            #print(f"res={res.val} overflow={overflow}")

            res.next = ListNode(0)
            res = res.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        head = reverseList(head)
        if head.val == 0 and head.next is not None: 
            head = head.next

        return head