# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def find_height(node):
            if node is None:
                return 0
            nonlocal nodes_w_h
            h = 1 + max(find_height(node.left), find_height(node.right))
            nodes_w_h[h].append(node.val)
            return h
            
            
        nodes_w_h = defaultdict(list) # nodes with height
        max_h = find_height(root)
        ans = []
        for h in range(1, max_h+1):
            ans.append(nodes_w_h[h])
            
        return ans
        
        