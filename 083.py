__author__ = 'lyb-mac'
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a=[]
        i=0
        while (head!=None):
            a[i] = head.val
            head = head.next
            i = i+1
        return sorted(list(set(a)))


