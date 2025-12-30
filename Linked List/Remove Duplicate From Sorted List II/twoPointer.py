# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        - Each node is visited at most once.
        - The inner while loop only advances `curr` forward, so total work remains linear.

        Space Complexity: O(1)
        - Uses constant extra space; modifications are done in place.
        """

        dummy = ListNode(-1)  # Sentinel node to handle deletions at head
        prev = dummy          # Points to the last node before the duplicate sequence
        dummy.next = head
        curr = head           # Pointer to traverse the list

        while curr and curr.next:
            # Case 1: Duplicate sequence detected
            if curr.val == curr.next.val:
                # Skip all nodes with the same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                # Remove the entire duplicate block
                prev.next = curr.next
            else:
                # Case 2: Current node is unique
                prev = prev.next

            curr = curr.next  # Move to the next node

        return dummy.next
