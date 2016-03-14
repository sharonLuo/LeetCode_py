"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#### iteratively
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        p = dummy
        tmp = dummy.next
        while p.next: # if there are still elements to check
            while tmp.next and tmp.next.val == p.next.val:
                tmp = tmp.next
            if tmp == p.next:
                p = p.next
                tmp = p.next
            else:
                p.next = tmp.next
        return dummy.next
  

### recursively
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
        if head == None or head.next == None:
            return head
        dummy = ListNode(head.val+1)
        dummy.next = head
        self.recurDelete(dummy, dummy.next)
        return dummy.next
        
    def recurDelete(self, prev, cur):
        if cur.next == None:
            return None
        start = cur.next
        while start and cur.val == start.val:
            start = start.next
        if start == cur.next:
            tmp = cur.next
            prev = prev.next
            cur = tmp
            self.recurDelete(prev, cur)
        else:
            if start == None:
                prev.next = None
                return
            prev.next = start
            cur = start
            self.recurDelete(prev, cur)
 