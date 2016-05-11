__author__ = 'lyb-mac'

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.instack,self.outstack=[],[]

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """


    def peek(self):
        """
        :rtype: int
        """


    def empty(self):
        """
        :rtype: bool
        """