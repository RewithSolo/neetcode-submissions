# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            next_jump = cur.next
            cur.next = prev
            prev = cur
            cur = next_jump

        
        first = head
        second = prev
        while second:
            next_jump_first = first.next
            next_jump_second = second.next

            first.next = second
            second.next = next_jump_first

            first = next_jump_first
            second = next_jump_second

    


