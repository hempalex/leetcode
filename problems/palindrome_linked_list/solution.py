# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # идем по списку slow/fast pointers
        # первым реверсим список
        # когда находим середину
        # идем в две стороны сравнивая элементы
        # проблема - нечетное количество элементов (элементы считаем в процессе)

        slow, fast = head, head

        # ищем середину списка
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    

        # если длина списка нечетная
        if fast and not fast.next:
            slow = slow.next 


        # переворачиваем список slow
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        slow = prev

        # сравниваем списки
        fast = head
        while slow and fast:
            if slow.val != fast.val: return False
            slow = slow.next
            fast = fast.next

        return True
        


        