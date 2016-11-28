__author__ = 'lyb-mac'
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:return head
        curr = head
        prev = None
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev