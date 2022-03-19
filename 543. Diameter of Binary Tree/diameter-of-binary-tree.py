# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Two case
1. pass root => longest chain in left + right + 1 - 1
2. no pass root => recursion root.left, root.right 
'''
class ExtendNode:
    def __init__(self, node, longest_chain=None):
        self.node = node
        self.left = None
        self.right = None

        if self.node.left:
            self.left = ExtendNode(self.node.left)
        if self.node.right:
            self.right = ExtendNode(self.node.right)
        self.longest_chain = longest_chain

        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def longest_chain(node):
            if node is None:
                return 0
            
            if node.longest_chain is None:
                left = longest_chain(node.left)
                right = longest_chain(node.right)
                node.longest_chain = 1 + max(left, right)

            return node.longest_chain
        
        if root is None:
            return 0
        
        if not isinstance(root, ExtendNode):
            root = ExtendNode(root)

        _max = 1 + longest_chain(root.left) + longest_chain(root.right) - 1

        _max = max(_max, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return _max
        
        