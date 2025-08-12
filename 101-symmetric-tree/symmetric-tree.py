# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root==None or self.Symmetric(root.left,root.right)

    def Symmetric(self, left: Optional[TreeNode],right: Optional[TreeNode])-> bool:
        if left==None or right==None:
            return left==right
        if left.val!=right.val:
            return False
        return (self.Symmetric(left.left,right.right) and self.Symmetric(left.right,right.left))