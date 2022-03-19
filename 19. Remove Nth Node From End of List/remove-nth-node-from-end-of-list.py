# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head
        front = cur
        for i in range(n):
            front = front.next
        
        while front is not None:
            prev = cur
            cur = cur.next
            front = front.next
        
        if prev is None:
            return cur.next
        else:
            prev.next = cur.next
            
        return head