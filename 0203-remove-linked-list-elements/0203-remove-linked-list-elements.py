class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        while head is not None and head.val == val:
            head = head.next
        if head is None:
            return None
        prev = head
        curr = head.next
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head