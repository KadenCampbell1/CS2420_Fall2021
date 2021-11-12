"""The HashMap class creates a HashMap object.

__init__ arguments:
None

Functions:
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

    def get(self, key):
        """returns the value for key if key is in the hashmap

        if key is not in the dictionary, a KeyError will occur.

        arguments:
        key -- type Any
        """
        pass

    def set(self, key, value):
        """adds the (key, value) pair to the hashmap

        After adding, if the load-factor is >= 80% it will rehash with a load-factor
        of k=2k-1 where k is the number of buckets.

        arguments:
        key -- type Any
        value -- type Any
        """
        # rehash when load-factor is >= 80%. new load-factor should be k=2k-1
        pass

    def remove(self, key):
        """removes the key and its associated value from the map

        if the key does not exist, nothing happens. This does not rehash the table
        after deleting the keys.

        arguments:
        key -- type Any
        """
        pass

    def clear(self):
        """empties the hashmap of all key-values"""
        pass

    def capacity(self):
        """returns the current capacity--number of buckets--in the map"""
        return self.capacity

    def size(self):
        """returns the number of key-value pairs in the map"""
        pass

    def keys(self):
        """returns a list of keys"""
        pass

    def __str__(self):
        """returns a list of key-value pairs"""
        return "return list of key-value pairs"
