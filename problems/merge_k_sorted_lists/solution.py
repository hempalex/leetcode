# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        ret = lists[0]

        for l in lists[1:]:
            ret = self.mergeTwoLists(ret, l)

        return ret


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        first = res = ListNode(None)

        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next

            res = res.next

        while list1:
            res.next = list1
            res = res.next
            list1 = list1.next

        while list2:
            res.next = list2
            res = res.next
            list2 = list2.next

        return first.next
