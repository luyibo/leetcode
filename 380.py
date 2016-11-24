__author__ = 'user'
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.d = {}
        self.count = 0
    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.d.has_key(val):
            return False
        else:
            self.l.append(val)
            self.d[val] = self.count
            self.count += 1
            return True


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.d.has_key(val):
            self.l.remove(val)
            del self.d[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if len(self.l) == 0: return -1
        return self.l[random.randint(0,len(self.l)-1)]