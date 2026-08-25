"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False
            return (isvalid(node.left, left, node.val) and isvalid(node.right, node.val, right))
        return isvalid(root, float("-inf"), float("inf"))

# Time Complexity: O(n), where n is the number of nodes in the binary tree. We visit each node once.
# Space Complexity: O(h), where h is the height of the binary tree. This space is used by the recursion stack. 
# In the worst case, the height of the tree can be n (for a skewed tree), leading to O(n) space complexity. 
# In a balanced tree, the height would be log(n), leading to O(log(n)) space complexity. 
