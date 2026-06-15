# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        value mod 10 - create a list node
        value//10 take as carry over
        """
        carry=0
        value = 0
        head = ListNode()
        temp = head
        while l1 or l2:
            val1, val2=0,0
            if l1:
                val1 = l1.val
            if l2:
                val2 =  l2.val
            value = val1+val2
            total= value + carry
            temp.next = ListNode(total%10)
            carry = total//10
            temp = temp.next
            if l1:
                l1= l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            temp.next = ListNode(carry)
        
        return head.next
        
        
       

