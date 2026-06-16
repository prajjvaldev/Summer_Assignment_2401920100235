class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare
        first = head
        second = prev

        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
