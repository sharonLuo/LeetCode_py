"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1, dummy2 = ListNode(0), ListNode(0)
        head1, head2, p = dummy1, dummy2, head
        while p:
            if p.val >= x:
                head2.next = p
                p = p.next
                head2 = head2.next
                head2.next = None
            else:
                head1.next = p
                p = p.next
                head1 = head1.next
                head1.next = None
        head1.next = dummy2.next
        head = dummy1.next
        return head