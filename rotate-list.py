"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        size = 0
        while p:
            size += 1
            p = p.next
        if size < 2 or k % size == 0:
            return head
        k = k % size
        count = 0
        slowhead = head
        while count < k:
            newhead = ListNode(0)
            newhead.next = slowhead
            slowhead = newhead
            count += 1
        slowp, fastp = slowhead, head
        while fastp.next:
            fastp = fastp.next
            slowp = slowp.next
        shifthead = slowp.next
        slowp.next = None
        newhead = slowhead
        while shifthead:
            newhead.val = shifthead.val
            newhead = newhead.next
            shifthead = shifthead.next
        return slowhead


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = head
        size = 0
        while p:
            size += 1
            p = p.next
        if size < 2 or k % size == 0:
            return head
        k = k % size
        p = head
        for step in range(size-k-1):
            p = p.next
        shifthead = p.next
        newhead = shifthead
        p.next = None
        while shifthead.next:
            shifthead = shifthead.next
        shifthead.next = head
        return newhead
        
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 0:
            return head
        p = head
        size = 1
        while p.next:
            size += 1
            p = p.next
        if size < 2 or k % size == 0:
            return head
        k = k % size
        p.next = head
        for step in range(size-k):
            p = p.next
        head = p.next
        p.next = None
        return head
        
        



        
        
                    


