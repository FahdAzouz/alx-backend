#!/usr/bin/env python3
'''task 1 module'''
import csv
import math
from typing import List
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    '''return a tuple of size two containing a start index and an end index'''
    first = (page-1) * page_size
    last = page * page_size
    return (first, last)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with default value 1 and
            page_size with default value 10.Use assert to verify that
            both arguments are integers greater than 0.
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0
        dataset = self.dataset()
        try:
            index = index_range(page, page_size)
            return dataset[index[0]:index[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """takes the same arguments (and defaults) as get_page
        and returns a dictionary"""
        dataset = self.dataset()
        size = len(dataset)
        total_pages = size // page_size + 1
        data = self.get_page(page, page_size)
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'prev_page': page - 1 if page > 1 else None,
            'next_page': page + 1 if page < total_pages else None,
            'total_pages': total_pages
        }
