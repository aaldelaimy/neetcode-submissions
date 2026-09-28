# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        m, start = slow, slow.next
        prev = None
        m.next = prev

        while start:
            temp = start.next
            start.next = prev
            prev, start = start, temp
        
        r = prev
        l = head

        while r:
            
            tempL, tempR = l.next, r.next
            l.next = r
            r.next = tempL
            l, r = tempL, tempR
        
        




