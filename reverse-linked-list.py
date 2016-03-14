"""
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""





# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#### iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while head is not None:
            next_node = head.next
            if res is None:
                res = head
                res.next = None
            else:
                head.next = res
                res = head
            head = next_node             
        return res
        
#### recursively approach 1
class Solution(object):
     def reverse_recursively(self, head, new_head):
        if not head:
            return new_head
        nxt = head.next
        head.next = new_head
        return self.reverse_recursively(nxt, head)

     def reverseList(self, head):
        return self.reverse_recursively(head, None)

#### recursively approach 2
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        
        tail = head.next
        head.next = None
        newhead = self.reverseList(tail)
        tail.next = head
        return newhead

