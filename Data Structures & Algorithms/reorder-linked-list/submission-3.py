class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # PHASE 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # PHASE 2: Split and Reverse the second half
        # We cut the list in two and flip the second half so we can 
        # iterate "backwards" towards the middle.
        second_half = slow.next
        slow.next = None # The "Cut": ends the first half
        
        prev = None
        curr = second_half
        while curr:
            temp = curr.next     # Save the original next node
            curr.next = prev     # Flip the pointer backward
            prev = curr          # Move prev forward
            curr = temp          # Move curr forward
        
        # PHASE 3: Merge (The Zipper)
        # Interleave nodes from the first half (first) and reversed second half (second)
        first = head
        second = prev # 'prev' is the head of the reversed second half
        
        while second:
            # Save the 'next' destinations for both lists
            tmp1 = first.next
            tmp2 = second.next
            
            # The Handshake: 
            # 1. Point first half node to second half node
            first.next = second
            # 2. Point second half node to the original next of the first half
            second.next = tmp1
            
            # Move both pointers forward to their saved positions
            first = tmp1
            second = tmp2