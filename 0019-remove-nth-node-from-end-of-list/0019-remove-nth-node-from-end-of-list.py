# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not n:
            return head
        temp=head
        length=0
        while temp:
            length+=1
            temp=temp.next
        
        
        count=0
        prev=ListNode()
        t= prev
        prev.next = head
        while count!=length-n:
            count+=1
            prev= prev.next
        if prev and prev.next:
            prev.next = prev.next.next
        else:
            return None
        return t.next