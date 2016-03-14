"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        
        carry = 0
        dummy = ListNode(0)
        l = dummy
        while l1 or l2 or carry:
            Sum, carry = carry, 0
            if l1:
                Sum += l1.val
                l1 = l1.next
            if l2:
                Sum += l2.val
                l2 = l2.next
            if Sum > 9:
                carry = 1
                Sum -= 10
            l.next = ListNode(Sum)
            l = l.next
        return dummy.next
        

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None: return l2
        if l2 == None: return l1
        
        flag = 0
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+flag) % 10)
            flag = (l1.val+l2.val+flag)/10
            l1 = l1.next
            l2 = l2.next
            p = p.next
        while l2:
            p.next = ListNode((l2.val+flag)%10)
            flag = (l2.val+flag)/10
            l2 = l2.next
            p = p.next
        while l1:
            p.next = ListNode((l1.val+flag)%10)
            flag = (l1.val+flag)/10
            l1 = l1.next
            p = p.next
        if flag == 1:
            p.next = ListNode(1)
        return dummy.next