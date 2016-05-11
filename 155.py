__author__ = 'lyb-mac'

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mini = [99999999999999]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if x<=self.mini[0]:
            self.mini.insert(0,x)


    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            if self.stack[-1]==self.mini[0]:
                self.mini = self.mini[1:]
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini[0]
import operator
operator.s