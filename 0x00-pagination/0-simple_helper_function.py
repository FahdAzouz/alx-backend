#!/usr/bin/env python3
'''task 0 module'''

from typing import Tuple

def index_range(page, page_size) -> Tuple[int, int]:
    '''return a tuple of size two containing a start index and an end index'''
    first = (page-1) * page_size
    last = page * page_size
    return (first, last)
