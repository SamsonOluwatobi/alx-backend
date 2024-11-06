#!/usr/bin/env python3
"""
Defines the MRUCache class, inheriting from BaseCaching, to implement a caching 
system with a Most Recently Used (MRU) eviction policy:

- Uses `self.cache_data`, a dictionary inherited from BaseCaching.
- You can override `__init__(self)`, but don't forget to call the parent `__init__` 
  using `super().__init__()`.

def put(self, key, item):
    - Adds the `item` to `self.cache_data` under the specified `key`.
    - If `key` or `item` is None, no action is taken.
    - If the number of items in `self.cache_data` exceeds `BaseCaching.MAX_ITEMS`,
      the most recently used (MRU) item is removed.
    - Prints "DISCARD:" followed by the evicted key when an item is discarded.

def get(self, key):
    - Retrieves the value in `self.cache_data` linked to the provided `key`.
    - Returns `None` if `key` is None or does not exist in `self.cache_data`.
    - Marks the accessed key as the most recently used by moving it to the front.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that inherits from BaseCaching and implements an MRU eviction 
    policy when the cache exceeds its limit.
    """
    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Remove the most recently used (MRU) item if the cache is full
                mru_key, _ = self.cache_data.popitem(False)
                print(f"DISCARD: {mru_key}")
            
            # Add the new item to the cache and mark it as recently used
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)  # Move to the front

        else:
            # Update the existing item and move it to the front
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieve an item by key."""
        if key is not None and key in self.cache_data:
            # Mark the accessed item as most recently used
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
