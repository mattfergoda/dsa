# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        return self.numberToList(self.getNumber(l1) + self.getNumber(l2))

    def getNumber(self, l):
        num = 0
        place = 1
        while l:
            num += (l.val * place)
            place *= 10
            l = l.next

        return num
        
    def numberToList(self, num):
        num = str(num)
        old_node = ListNode(num[0])
        for i in range(1, len(num)):
            new_node = ListNode(num[i])
            new_node.next = old_node
            old_node = new_node

        return new_node