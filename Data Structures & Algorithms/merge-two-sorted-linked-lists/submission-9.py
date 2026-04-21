# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2
        head = list1 if list1.val < list2.val else list2
        tail = head

        while list1 and list2:
            if head == list1:
                list1 = list1.next
                continue
            elif head == list2:
                list2 = list2.next
                continue

            if list1.val > list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            tail = tail.next

        tail.next = list2 or list1
        return head
