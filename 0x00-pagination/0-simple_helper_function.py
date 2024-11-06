#!/usr/bin/env python3
"""
This module includes a function, `index_range`, which accepts two integer
parameters: `page` and `page_size`. The function returns a two-element tuple
representing the starting and ending indices, which define the range of indexes
to retrieve in a list based on specific pagination parameters.

Note: Pages are 1-indexed, meaning the first page is represented as page 1.
"""

def index_range(page: int, page_size: int) -> tuple:
    """
    Calculates the start and end index for a given page and page size.

    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing two integers, the start index and the end index
               that indicate the range of items for the specified page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return start_index, end_index
