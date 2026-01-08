# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        prev = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = prev.next
            curr = nxt

        return prev