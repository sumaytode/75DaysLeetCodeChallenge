# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next   # Step 1: store next
            curr.next = prev        # Step 2: reverse link
            prev = curr             # Step 3: move prev
            curr = next_node        # Step 4: move curr
        
        return prev