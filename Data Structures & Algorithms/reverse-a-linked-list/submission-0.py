# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None
        temp = head
        prev = None

        while(temp):
            
            nxt= temp.next
            temp.next = prev
            tempHead = temp
            prev = temp
            temp = nxt

        return tempHead
        