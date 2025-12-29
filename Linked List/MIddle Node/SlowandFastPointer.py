class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node using fast and slow pointers.
        If there are two middle nodes, returns the second one.
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
