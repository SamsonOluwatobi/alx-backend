#!/usr/bin/env python3
"""
Defines the LRUCache class, inheriting from BaseCaching, implementing a caching 
system with a Least Recently Used (LRU) eviction policy:

- Uses `self.cache_data`, a dictionary inherited from BaseCaching.
- You can override `__init__(self)`, but don’t forget to call the parent `__init__` 
  using `super().__init__()`.

def put(self, key, item):
    - Adds the `item` to `self.cache_data` under the given `key`.
    - If `key` or `item` is None, no action is performed.
    - If the number of items in `self.cache_data` exceeds `BaseCaching.MAX_ITEMS`,
      the least recently used (LRU) item is removed.
    - Prints "DISCARD:" followed by the evicted key when an item is discarded.

def get(self, key):
    - Retrieves the value in `self.cache_data` associated with the provided `key`.
    - Returns `None` if `key` is None or does not exist in `self.cache_data`.
    - Marks the accessed key as recently used by moving it to the front.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class extending BaseCaching to implement LRU eviction in the cache"""
    def __init__(self):
        """Initialize the LRUCache class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache, evicting the least recently used item if necessary"""
        if key is None or item is None:
            return
        
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                # Remove the least recently used (LRU) item if the cache is full
                first_key, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {first_key}")

            # Add the new item to the cache
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)  # Move to the front to mark as recently used
        else:
            self.cache_data[key] = item  # Update existing item

    def get(self, key):
        """Retrieve the value linked to the given key, marking it as recently used"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the front to mark it as recently used
        self.cache_data.move_to_end(key, last=False)
        return self.cache_data[key]
