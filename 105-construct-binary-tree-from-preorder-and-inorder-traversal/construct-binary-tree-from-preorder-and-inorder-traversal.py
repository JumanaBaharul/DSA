# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap={}
        for idx,val in enumerate(inorder):
            inMap[val]=idx
        def arrayToTree(preStart:int,preEnd:int,inStart:int,inEnd:int)->Optional[TreeNode]:
            if preStart>preEnd or inStart>inEnd:
                return None
            rootVal=preorder[preStart]
            root=TreeNode(rootVal)
            inRoot=inMap[rootVal]
            numsLeft=inRoot-inStart
            root.left=arrayToTree(preStart+1,preStart+numsLeft,inStart,inRoot-1)
            root.right=arrayToTree(preStart+numsLeft+1,preEnd,inRoot+1,inEnd)
            return root
        return arrayToTree(0,len(preorder)-1,0,len(inorder)-1)