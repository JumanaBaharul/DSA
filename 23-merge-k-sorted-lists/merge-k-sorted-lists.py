# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        count=0
        for node in lists:
            if node:
                heapq.heappush(heap,(node.val,count,node))
                count+=1
        dummyNode=ListNode(-1)
        temp=dummyNode
        while heap:
            val,_,node=heapq.heappop(heap)
            temp.next=node
            temp=temp.next
            if node.next:
                heapq.heappush(heap,(node.next.val,count,node.next))
                count+=1
        return dummyNode.next