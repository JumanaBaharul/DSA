# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        st=[root]
        while st:
            cur=st.pop()
            if cur.right:
                st.append(cur.right)
            if cur.left:
                st.append(cur.left)
            if st:
                cur.right=st[-1]
            cur.left=None