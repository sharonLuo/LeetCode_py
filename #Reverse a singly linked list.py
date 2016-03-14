#Reverse a singly linked list
#Hint:
#A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# reverse iteratively
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res = None
        while head is not None:
            next_node = head.next
            head.next = res
            res = head
            head = next_node
                      
        return res
        
# reverse recursively
class Solution(object):
     def reverse_recursively(self, head, new_head):
        if not head:
            return new_head
        nxt = head.next
        head.next = new_head
        return self.reverse_recursively(nxt, head)

     def reverseList(self, head):
        return self.reverse_recursively(head, None)
     