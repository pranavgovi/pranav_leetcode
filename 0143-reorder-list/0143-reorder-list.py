# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        1 2 3 4 5 6  7
        1 2 3 4
        7 6 5
        go till the middle , store the next ptr
        point the middle value ot none
        seocnd LL reverse it
        """
        #slow will give the middle
        slow, fast = head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #now slow will have the middle
        t1= slow.next
        slow.next=None
        #now we have 2 LL
        #second LL reverse it starting from t1
        prev=None
        while t1:
            t2 = t1.next
            t1.next = prev
            prev= t1
            t1= t2
        #Now prev will be the start of the second LL
        l1= head
        l2= prev

        while l1 and l2:
            t1=l1.next
            t2=l2.next
            l1.next = l2
            l2.next = t1 
            l1, l2= t1,t2
        return head
        