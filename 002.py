__author__ = 'lyb-mac'
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
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=[]
        while (l1!=None and l2!=None):
            a.append(l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next
        while(l1!=None):
            a.append(l1.val)
            l1 = l1.next
        while(l2!=None):
            a.append(l2.val)
            l2 = l2.next
        if len(a)==1:
            if a[0]>=10:
                 return [a[0]%10,a[0]/10]
            else:return a
        else:
            for i in range(len(a)):
                if (a[i]>=10):
                    if (i<=(len(a)-2)):
                        a[i+1] = a[i]/10+a[i+1]
                        a[i] = a[i]%10

                    else:
                        temp = a[i]
                        a[i] = a[i]%10
                        a.append(temp/10)
            return a