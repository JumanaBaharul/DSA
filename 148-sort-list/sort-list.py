# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        middle=self.findMiddle(head)
        right=middle.next
        middle.next=None
        left=head
        left=self.sortList(head)
        right=self.sortList(right)
        return self.mergeTwoSortedLinkedLists(left,right)

    def mergeTwoSortedLinkedLists(self,l1,l2):
        dummyNode=ListNode(-1)
        temp=dummyNode
        while l1!=None and l2!=None:
            if l1.val<=l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        if l1!=None:
            temp.next=l1
        else:
            temp.next=l2
        return dummyNode.next
    
    def findMiddle(self,head):
        if head==None or head.next==None:
            return head
        slow=head
        fast=head.next
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow