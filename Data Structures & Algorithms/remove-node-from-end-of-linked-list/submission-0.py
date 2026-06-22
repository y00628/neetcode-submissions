# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        cnt = 0

        while curr:
            curr = curr.next
            cnt += 1

        # cnt - n + 1

        prev = None
        curr = head

        for i in range(cnt-n):
            if curr:
                prev = curr
                curr = curr.next

        if prev and curr:
            prev.next = curr.next
        elif curr:
            head = curr.next

        

        # p -> c -> n
        return head
             

        