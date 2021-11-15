"""The HashMap class creates a HashMap object.

__init__ arguments:
None

Functions:
calculation(key) -- returns the index for the values of key
get(key) -- returns the value for key if key is in the hashmap.
set(key, value) -- adds the (key, value) pair to the hashmap.
remove(key) -- removes the key and its associated value from the map.
clear() -- empties the hashmap.
capacity() -- returns the current capacity in the map.
size() -- returns the number of key-value pairs in the map.
key() -- returns a list of keys.
__str__() -- returns a list of key-value pairs.
"""


class HashMap:
    def __init__(self):
        self.capacity = 7
        self.key_lyst = [None] * self.capacity
        self.value_lyst = [None] * self.capacity

    def calculation(self, key):
        """returns the index for the values of key in the hashmap

        arguments:
        key -- type Any
        """
        pass

    def get(self, key):
        """returns the value for key if key is in the hashmap

        if key is not in the dictionary, a KeyError will occur.

        arguments:
        key -- type Any
        """
        if key in self.key_lyst:
            # calculate index of value_lyst and return value at index
            pass
        raise KeyError("Key is not in HashMap")

    def set(self, key, value):
        """adds the (key, value) pair to the hashmap

        After adding, if the load-factor is >= 80% it will rehash with a load-factor
        of k=2k-1 where k is the number of buckets.

        arguments:
        key -- type Any
        value -- type Any
        """

        # rehash when load-factor is >= 80%. new load-factor should be k=2k-1
        # If calculation give a collision value rewrite calculation in here using probing
        # save what values have new locations
        pass

    def remove(self, key):
        """removes the key and its associated value from the map

        if the key does not exist, nothing happens. This does not rehash the table
        after deleting the keys.

        arguments:
        key -- type Any
        """

        self.value_lyst.pop(self.get(key))
        self.key_lyst.pop(key)

    def clear(self):
        """empties the hashmap of all key-values"""

        self.capacity = 7
        self.key_lyst = []
        self.value_lyst = [None] * self.capacity

    def capacity(self):
        """returns the current capacity--number of buckets--in the map"""

        return self.capacity

    def size(self):
        """returns the number of key-value pairs in the map"""

        return len(self.key_lyst)

    def keys(self):
        """returns a list of keys"""

        return self.key_lyst

    def __str__(self):
        """returns a string list of key-value pairs"""

        temp = []
        for i in self.key_lyst:
            temp.append((i, self.get(i)))
        return str(temp)
