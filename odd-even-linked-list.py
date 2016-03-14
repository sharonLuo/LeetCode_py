"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
### 68 ms
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return head
        odd = oddHead = head
        even = evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return oddHead



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        p, q = head, head
        while q:
            q = q.next
            if not q or not q.next: break
            next_p, next_q = p.next, q.next
            q.next = next_q.next
            p.next ,next_q.next = next_q , next_p
            p = p.next
        return head
        


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
### 68ms
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        if node is None:
            return head
        lastOdd = head
        firstEven = head.next
        pre = head
        node = firstEven
        i = 2
        while node:
            if i % 2 != 0:
                lastOdd.next = node
                lastOdd = node
                pre.next = node.next
                node.next = firstEven
                node = pre.next
                i += 1
            else:
                i += 1
                pre = node
                node = node.next
        return head
