# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr, prev = head, None
        
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        mul = 1
        num = 0
        while prev:
            if prev.val:
                num += mul
            mul *= 2
            prev = prev.next
        
        return num