__author__ = 'lyb-mac'
def mergeTwoLists(self, l1, l2):
        a = []
        while(l1!=None and l2!=None):
            a.append(l1.val)
            a.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        if(l1!=None):
            while(l1!=None):
                a.append(l1.val)
                l1 = l1.next
        else:
            while(l2!=None):
                a.append(l2.val)
                l2 = l2.next
        return sorted(a)