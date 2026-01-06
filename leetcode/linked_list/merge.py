# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()

        l1_curr = list1
        l2_curr = list2

        while l1_curr and l2_curr:
            if l1_curr.val < l2_curr.val:
                tail.next = l1_curr
                l1_curr = l1_curr.next
            else:
                tail.next = l2_curr
                l2_curr = l2_curr.next
            tail = tail.next

        tail.next = l1_curr if l1_curr else l2_curr
        return dummy.next