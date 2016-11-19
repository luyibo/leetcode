__author__ = 'lyb-mac'

class Solution(object):

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:return False
        slow = head
        fast = head
        while  fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:return True
        return False