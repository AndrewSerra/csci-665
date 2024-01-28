import random
import math
from typing import Any
from sort_verifier import is_sorted
from insertion_sort import insertion_sort


def bucket_sort(arr: list[Any]) -> list[Any]:
    
    if len(arr) <= 1:
        return arr
    
    size = len(arr)
    buckets = [[] for _ in range(size)]

    for d in arr:
        bucket_id = math.floor(size * d)
        buckets[bucket_id].append(d)
        insertion_sort(buckets[bucket_id])

    _sorted = []
    for bucket in buckets:
        _sorted = [*_sorted, *bucket]

    return _sorted
