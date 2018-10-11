# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1;
        q = l2;
        rst = ListNode()
        cur = rst
        upcarry = 0
        while(l1 or l2 or upcarry):
            if l1:
                upcarry += l1.val
                l1 = l1.next
            if l2:
                upcarry += l2.val
                l2 = l2.next
            cur.next = ListNode(upcarry%10)
            cur = cur.next
            upcarry //= 10
        return rst.next