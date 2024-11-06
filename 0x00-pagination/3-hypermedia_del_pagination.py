#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination

This module implements pagination that is resilient to deletions in the dataset.
When a row is removed between requests, the pagination adjusts to avoid skipping items.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset if it hasn’t been loaded."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Returns a dictionary of the first 1000 dataset items, indexed by row."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(min(1000, len(dataset)))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Provides a paginated subset of the dataset, resilient to deletions.
        
        Args:
            index (int, optional): The starting index of the requested page.
            page_size (int, optional): The number of items per page.

        Returns:
            dict: Contains the start index, next index, current page size, and data list.
        """
        index_data = self.indexed_dataset()
        assert index is not None and 0 <= index < len(index_data), "Index out of range."

        data_page = []
        current_index = index
        data_fetched = 0

        # Gather data until the page size is met or dataset ends
        while data_fetched < page_size and current_index < len(index_data):
            if current_index in index_data:
                data_page.append(index_data[current_index])
                data_fetched += 1
            current_index += 1

        next_index = current_index if current_index < len(index_data) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data_page),
            'data': data_page,
        }
