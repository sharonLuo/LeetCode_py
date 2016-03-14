"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


## iterative
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        while start:
            begin = start
            while begin.next and begin.val == begin.next.val:
                begin = begin.next
            start.next = begin.next
            start = start.next
        return head


### recursive
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        dummy = ListNode(head.val+1)
        dummy.next = head
        self.recurDelete(dummy, head)
        return dummy.next
        
    def recurDelete(self, prev, cur):
        if cur == None:
            return cur
        if prev.val == cur.val:
            prev.next = cur.next
            self.recurDelete(prev, prev.next)
        else:
            self.recurDelete(cur, cur.next)
  
  