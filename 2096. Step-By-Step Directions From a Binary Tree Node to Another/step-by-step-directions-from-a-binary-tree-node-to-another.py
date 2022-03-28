# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(cur: TreeNode, destValue: int , path):
            if cur is None:
                return None
            
            if cur.val == destValue:
                return True
            
            path.append("L")
            if find_path(cur.left, destValue, path):
                return True
            path.pop()
            path.append("R")
            if find_path(cur.right, destValue, path):
                return True
            path.pop()
     
            return None
    
        def remove_common(path1, path2):
            while path1 and path2 and path1[0] == path2[0]:
                path1.popleft()
                path2.popleft()


        s_path = deque()
        find_path(root, startValue, s_path)
        d_path = deque()
        find_path(root, destValue, d_path)
        remove_common(s_path, d_path)
        if len(s_path) == 0: 
            # s is some parent of d
            return "".join(d_path)
        elif len(d_path) == 0:
            # d is some parent of s
            return "U"*len(s_path)
        else:
            # s & d share a common parent
            return "U" * len(s_path) + "".join(d_path)
            
            


            
                

                    
                
                