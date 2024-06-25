#!/usr/bin/env python3
"""LFU Cache implementation"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU (Least Frequently Used) caching system"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage = {}
        self.lru = {}

    def put(self, key, item):
        """
        Cache a key-value pair
        If MAX_ITEMS is reached, discard the least frequently used item
        If there's a tie, discard the least recently used among the tied items
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS and key not in self.cache_data:
            lfu_key = min(self.usage, key=self.usage.get)
            lfu_keys = [k for k, v in self.usage.items() if v == self.usage[lfu_key]]
            if len(lfu_keys) > 1:
                lru_among_lfu = min(lfu_keys, key=lambda k: self.lru[k])
                del self.cache_data[lru_among_lfu]
                del self.usage[lru_among_lfu]
                del self.lru[lru_among_lfu]
                print(f"DISCARD: {lru_among_lfu}")
            else:
                del self.cache_data[lfu_key]
                del self.usage[lfu_key]
                del self.lru[lfu_key]
                print(f"DISCARD: {lfu_key}")

        self.cache_data[key] = item
        self.usage[key] = self.usage.get(key, 0) + 1
        self.lru[key] = max(self.lru.values()) + 1 if self.lru else 1

    def get(self, key):
        """
        Return the value linked to the given key, or None
        Update usage count and LRU order on access
        """
        if key is not None and key in self.cache_data:
            self.usage[key] = self.usage.get(key, 0) + 1
            self.lru[key] = max(self.lru.values()) + 1
            return self.cache_data[key]
        return None
