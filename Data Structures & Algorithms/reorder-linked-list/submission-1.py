# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow.next
        slow.next = None
        
        slow = temp
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # [1,2,3] [6, 5, 4] 
        # [1,6,5,4] [2,3]
        # [1,6,2,3] [5,4]
        # [1,6,2,5,4] [3]
        # [1,6,2,5,3] [4]
        second = prev
        first = head
        while second:
            temp = first.next
            first.next = second
            second = temp
            first = first.next