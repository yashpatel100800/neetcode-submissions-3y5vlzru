"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        headOld = head
        copyMap = {}
        while(headOld):
            headNew = Node(headOld.val)
            copyMap[headOld] = headNew
            headOld = headOld.next
        headNew = copyMap[head]
        headOld = head

        while(headOld):
            if headOld.next != None:
                copyMap[headOld].next = copyMap[headOld.next]
            else:
                copyMap[headOld].next = None
            if headOld.random != None:
                copyMap[headOld].random = copyMap[headOld.random]
            else:
                copyMap[headOld].random = None
            headOld = headOld.next

        return headNew