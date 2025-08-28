# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self,root:Optional[TreeNode],forward:bool):
        self.st=[]
        self.forward=forward
        self.pushAll(root)
    
    def pushAll(self,node:Optional[TreeNode]):
        while node:
            self.st.append(node)
            node=node.left if self.forward else node.right
        
    def next(self)->int:
        node=self.st.pop()
        val=node.val
        if self.forward:
            self.pushAll(node.right)
        else:
            self.pushAll(node.left)
        return val

    def hasNext(self)->bool:
        return len(self.st)>0

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        left=BSTIterator(root,True)
        right=BSTIterator(root,False)
        i=left.next() if left.hasNext() else None
        j=right.next() if right.hasNext() else None
        while i is not None and j is not None and i<j:
            s=i+j
            if s==k:
                return True
            elif s<k:
                i=left.next() if left.hasNext() else None
            else:
                j=right.next() if right.hasNext() else None
        return False