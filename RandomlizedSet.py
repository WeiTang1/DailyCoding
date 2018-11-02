# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1141/
import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        map = {}
        array = []
        length = 0


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if self.map.has_key(val):
            return False
        self.length += 1
        map[val] = self.length-1
        self.arry[self.length-1] = val
        return True



    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.map.has_key(val):
            return False
        index = self.map.get(val)
        del map[val]
        self.array[index] = self.array[-1]
        self.length -= 1
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        ran = random.randint(0,self.length-1)
        return self.arr[ran]

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(val)
param_2 = obj.remove(val)
param_3 = obj.getRandom()