# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

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


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        elif len(lists) == 1:
            return lists[0]

        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])

        a = lists[0:len(lists)//2]
        b = lists[len(lists)//2:]
        return self.mergeTwoLists(self.mergeKLists(a), self.mergeKLists(b))
