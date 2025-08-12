# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if root==None:
            return res
        self.recursionRight(root,0,res)
        return res
    def recursionRight(self,root,level,res):
        if not root:
            return
        if len(res)==level:
            res.append(root.val)
        self.recursionRight(root.right,level+1,res)
        self.recursionRight(root.left,level+1,res)