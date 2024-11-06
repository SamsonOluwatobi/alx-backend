#!/usr/bin/env python3
"""
Defines the LIFOCache class, which extends BaseCaching and implements a caching 
system using the last-in, first-out (LIFO) eviction policy:

- Uses `self.cache_data` dictionary from BaseCaching.
- You can override `__init__(self)`, but don’t forget to call the parent `__init__` 
  using `super().__init__()`.

def put(self, key, item):
    - Stores `item` in `self.cache_data` under the given `key`.
    - If `key` or `item` is None, no action is performed.
    - If `self.cache_data` exceeds `BaseCaching.MAX_ITEMS`, the last added 
      item (based on LIFO) is discarded.
    - Prints "DISCARD:" followed by the discarded key when an item is evicted.

def get(self, key):
    - Retrieves the value from `self.cache_data` for the provided `key`.
    - Returns `None` if `key` is None or not present in `self.cache_data`.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """LIFOCache class extending BaseCaching for a LIFO caching system."""
    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache, evicting the last item if the limit is reached."""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Evict the last inserted item in the cache
                lastKey, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {lastKey}")
        
        # Add the item to the cache and move it to the end (LIFO order)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve the value associated with the given key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
