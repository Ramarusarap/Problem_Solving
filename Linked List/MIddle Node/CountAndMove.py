# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a singly linked list.
        If there are two middle nodes, returns the second one.

        Approach:
        1. Count total number of nodes.
        2. Move to (count // 2) steps from head.
        """

        count = 0
        temp = head

        # Step 1: Count nodes
        while temp:
            count += 1
            temp = temp.next

        # Step 2: Move to middle
        steps = count // 2
        while steps > 0:
            head = head.next
            steps -= 1

        return head
