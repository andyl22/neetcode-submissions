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
        first, second = head, prev
        while second:
            # 1. Save the next nodes for BOTH halves
            tmp1 = first.next
            tmp2 = second.next
            
            # 2. Re-wire the connections
            first.next = second  # First points to Second
            second.next = tmp1   # Second points to original next of First
            
            # 3. Move both pointers forward to their saved 'next' nodes
            first = tmp1
            second = tmp2