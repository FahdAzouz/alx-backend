#!/usr/bin/env python3
'''task 0 module'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    Methods:
        put(key, item) - store a key-value pair
        get(key) - retrieve the value associated with a key
    """
    def __init__(self):
        '''initialize'''
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''put data in the cache'''
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        '''get item from cache'''
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
