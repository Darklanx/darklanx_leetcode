# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def get_max(node):
            left = 0
            right = 0
            if node.left is not None:
                left = max(left, get_max(node.left))
            if node.right is not None:
                right = max(right, get_max(node.right))
            
            nonlocal _max
            _max = max(_max, left + node.val + right)
            return node.val + max(left, right)
                
        _max = -math.inf 
        get_max(root)
        return _max
        