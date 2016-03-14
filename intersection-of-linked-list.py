"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        lenA, lenB = 0, 0
        while curA != None:
            lenA += 1
            curA = curA.next
        while curB != None:
            lenB += 1
            curB = curB.next
        curA, curB = headA, headB
        if lenA > lenB:
            for inx in range(lenA-lenB):
                curA = curA.next
        if lenB > lenA:
            for inx in range(lenB-lenA):
                curB = curB.next
        while curA.val != curB.val:
            curA = curA.next
            curB = curB.next
        return curA


 官方版：
蛮力法枚举（O(mn) 时间, O(1) 空间）

对于链表A中的每个节点ai，遍历整个链表B，检查B中是否有节点与ai重合

哈希表解法（O(n+m) 时间, O(n) or O(m) 空间）

遍历链表A并将每个节点的地址/引用存储在哈希表中。然后检查链表B中的每个节点bi：如果bi出现在哈希表中，则bi就是交点。

双指针解法 (O(n+m) 时间, O(1) 空间):

维护两个指针pA和pB，初始分别指向A和B。然后让它们分别遍历整个链表，每步一个节点。

当pA到达链表末尾时，让它指向B的头节点（没错，是B）；类似的当pB到达链表末尾时，重新指向A的头节点。

如果pA在某一点与pB相遇，则pA/pB就是交点。

下面来看下为什么这个算法可行，考虑两个链表：A = {1,3,5,7,9,11} B = {2,4,9,11}，它们的交点是节点'9'。由于B的长度是4 小于 A的长度6，pB会首先到达链表的末尾，由于pB比pA恰好少走2个节点。通过把pB指向A的头，把pA指向B的头，我们现在让pB比pA恰好多走2个节点。所以在第二轮，它们可以保证同时在交点相遇。

如果两个链表有交点，则它们的最后一个节点一定是同一个节点。所以当pA/pB到达链表末尾时，分别记录下A和B的最后一个节点。如果两个链表的末尾节点不一致，说明两个链表没有交点。

本人解题思路：
将链表A的末尾节点endA指向B的头结点headB

交点存在性的判断：
如果此时的链表中存在环路，则说明两个链表相交

交点的确定：
pA指针从headA出发，向前走lenB步（链表B的长度）

将pB指针指向headA，令pA和pB同时向前行进（每次一步），记下它们首次相遇的位置，即为链表的交点

原理：
当pA与pB相遇时，pA恰好比pB领先一个整环的长度(lenB)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA == 0 or lenB == 0:
            return None
        endA = self.getListEnd(headA)
        endA.next = headB
        hasCircle = False
        p = headA
        cnt = 0
        while p:
            cnt += 1
            if cnt > lenA + lenB:
                hasCircle = True
                break
            p = p.next
        if not hasCircle:
            endA.next = None
            return None
        p1 = headA
        for x in range(lenB):
            p1 = p1.next
        p2 = headA
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        endA.next = None
        return p1

    def getListEnd(self, head):
        end = head
        while end.next:
            end = end.next
        return end

    def getListLen(self, head):
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        return size
        

