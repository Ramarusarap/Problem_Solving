# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs inorder traversal of a binary tree.
        Inorder traversal order: Left -> Root -> Right
        """

        elements = []

        def inOrder(node):
            # Base case: if the current node is None, return
            if not node:
                return

            # Traverse left subtree
            inOrder(node.left)

            # Visit current node
            elements.append(node.val)

            # Traverse right subtree
            inOrder(node.right)

        # Start traversal from the root
        inOrder(root)
        return elements

Time Complexity
O(n)
Every node is visited exactly once.

Space Complexity

O(n)
In the worst case (skewed tree), recursion stack can grow to n.
Output list also stores n values.
