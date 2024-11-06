#!/usr/bin/env python3
"""
Define a BasicCache class inheriting from BaseCaching as a simple caching system.

- Use the `self.cache_data` dictionary from the BaseCaching class.
- This caching system has no size limit.

def put(self, key, item):
    - Store `item` in `self.cache_data` under the specified `key`.
    - If `key` or `item` is None, the method should take no action.

def get(self, key):
    - Retrieve the value in `self.cache_data` associated with `key`.
    - If `key` is None or doesn’t exist in `self.cache_data`, return None.
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that extends BaseCaching as a basic caching system."""
    def put(self, key, item):
        """Store an item in the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by its key."""
        if key is None:
            return None
        return self.cache_data.get(key)

