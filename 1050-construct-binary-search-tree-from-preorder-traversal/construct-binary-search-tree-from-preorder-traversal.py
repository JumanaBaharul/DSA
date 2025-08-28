# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(preorder,bound,idx):
            if idx[0]==len(preorder) or preorder[idx[0]]>bound:
                return None
            root_val=preorder[idx[0]]
            root=TreeNode(root_val)
            idx[0]+=1
            root.left=build(preorder,root_val,idx)
            root.right=build(preorder,bound,idx)
            return root
        return build(preorder,float('inf'),[0])