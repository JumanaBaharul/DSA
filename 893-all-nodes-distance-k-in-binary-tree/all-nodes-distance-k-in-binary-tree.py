# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque,defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_track={}
        def mark_parents(node,parent=None):
            if not node:
                return 
            if parent:
                parent_track[node]=parent
            mark_parents(node.left,node)
            mark_parents(node.right,node)
        mark_parents(root)

        q=deque([target])
        vis=set()
        vis.add(target)
        curr_level=0
        while q:
            if curr_level==k:
                break
            size=len(q)
            for _ in range(size):
                curr=q.popleft()
                if curr.left and curr.left not in vis:
                    q.append(curr.left)
                    vis.add(curr.left)
                if curr.right and curr.right not in vis:
                    q.append(curr.right)
                    vis.add(curr.right)
                if curr in parent_track and parent_track[curr] not in vis:
                    q.append(parent_track[curr])
                    vis.add(parent_track[curr])
            curr_level += 1
        return [node.val for node in q]