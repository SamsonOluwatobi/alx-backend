#!/usr/bin/env python3
"""
Defines the FIFOCache class, inheriting from BaseCaching, as a caching system
with a first-in, first-out (FIFO) eviction policy:

- Uses `self.cache_data` dictionary from the BaseCaching class.
- Overrides the __init__ method, calling the parent’s __init__ with `super().__init__()`.

def put(self, key, item):
    - Adds `item` to `self.cache_data` using `key`.
    - If `key` or `item` is None, the method does nothing.
    - If `self.cache_data` exceeds BaseCaching.MAX_ITEMS, the first item added 
      (based on FIFO) is removed.
    - Prints "DISCARD:" followed by the discarded key when an item is evicted.

def get(self, key):
    - Retrieves the value in `self.cache_data` associated with `key`.
    - Returns None if `key` is None or doesn't exist in `self.cache_data`.
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class extending BaseCaching to implement a FIFO caching system.
    """
    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache, discarding the oldest if the limit is exceeded."""
        if key is not None and item is not None:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Evict the first inserted item from the cache
            first_item, _ = self.cache_data.popitem(False)
            print(f"DISCARD: {first_item}")

    def get(self, key):
        """Retrieve an item from the cache by its key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
