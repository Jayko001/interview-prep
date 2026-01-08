# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the lenght of list
        n = 1
        curr = head
        while curr:
            curr = curr.next
            n += 1

        # find middle point
        length = n // 2

        # split the list into 2
        prev = None
        curr = head
        for _ in range(length):
            prev = curr
            curr = curr.next

        l2 = curr
        prev.next = None

        # reverse the 2nd list
        prev = None
        curr = l2

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        l2 = prev

        # Merge the 2 lists
        l1 = head
        l2 = l2  # head of reversed second half

        while l2:  # second half is <= first half length
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next

        tmp = head
        while tmp:
            print(tmp.val)
            tmp = tmp.next
        print("end of head")


