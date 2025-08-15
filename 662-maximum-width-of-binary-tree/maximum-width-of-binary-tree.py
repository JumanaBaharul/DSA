# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        if root==None:
            return res
        q=deque([(root,0)])
        while q:
            size=len(q)
            mini=q[0][1]
            first=last=0
            for i in range(size):
                node,cur=q.popleft()
                cur=cur-mini
                if i==0:
                    first=cur
                if i==size-1:
                    last=cur
                if node.left:
                    q.append((node.left,cur*2+1))
                if node.right:
                    q.append((node.right,cur*2+2))
            res=max(res,last-first+1)
        return res