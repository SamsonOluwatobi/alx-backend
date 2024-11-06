#!/usr/bin/env python3
"""
Simple pagination:

This module implements a `get_page` method that takes two optional integer
arguments: `page` (default is 1) and `page_size` (default is 10).

This method uses a CSV file containing a list of popular baby names as the data source.
It asserts that the inputs are positive integers and leverages the `index_range` function
to calculate the correct indices for pagination, returning the specified page of the dataset.

If the indices calculated fall outside the dataset range, an empty list is returned.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Determines the starting and ending indices for pagination.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and the end index, defining
               the range of items for the specified page.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index


class Server:
    """Server class to manage and paginate a dataset of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads and caches the dataset if it hasn't been loaded already.

        Returns:
            list: A cached list of records from the CSV file, each entry representing a row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as file:
                reader = csv.reader(file)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page from the dataset.

        Args:
            page (int): The page number to retrieve.
            page_size (int): The number of items per page.

        Returns:
            list: A list containing the rows for the specified page, or an empty list
                  if the page is outside the dataset range.
        """
        # Ensure both page and page_size are positive integers.
        assert isinstance(page, int) and page > 0, "Page must be a positive integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer."

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
