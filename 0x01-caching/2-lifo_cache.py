#!/usr/bin/env python3
'''task 2 module'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''lifo type of caching'''

    def __init__(self):
        '''initialization'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[-1]))
                del self.cache_data[self.order[-1]]
                del self.order[-1]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key.
        If key is None or doesn't exist, return None
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
