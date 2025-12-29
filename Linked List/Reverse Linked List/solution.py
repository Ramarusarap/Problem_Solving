# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list iteratively.

        Approach:
        - Maintain a pointer `prev` to track the reversed portion.
        - Traverse the list and reverse links one by one.

        Args:
            head (Optional[ListNode]): Head of the singly linked list

        Returns:
            Optional[ListNode]: New head of the reversed linked list
        """

        prev = None               # Will become the new head
        curr = head               # Pointer to traverse the list

        while curr:
            next_node = curr.next # Store next node
            curr.next = prev      # Reverse the link
            prev = curr           # Move prev forward
            curr = next_node      # Move curr forward

        return prev
