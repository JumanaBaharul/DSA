# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root,float("-inf"),float("inf"))

    def _isValidBST(self,root:TreeNode,minVal:float,maxVal:float)->bool:
        if not root:
            return True            
        if root.val<=minVal or root.val>=maxVal:
            return False
        return (self._isValidBST(root.left,minVal,root.val) and
                self._isValidBST(root.right,root.val,maxVal))