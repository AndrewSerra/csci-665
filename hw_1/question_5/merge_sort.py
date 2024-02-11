__author__="Andrew Serra"

from typing import Any

def _split_arr(arr: list[Any]) -> tuple[list[Any]]:
    mid = len(arr) // 2
    return merge_sort(arr[:mid]), merge_sort(arr[mid:])

def merge_sort(arr: list[Any]) -> list[Any]:

    if len(arr) <= 1:
        return arr
    
    left, right = _split_arr(arr)
    combined = []

    left_idx, right_idx = 0, 0

    while left_idx < len(left) or right_idx < len(right):

        if left_idx < len(left) and right_idx >= len(right):
            combined.append(left[left_idx])
            left_idx += 1
        elif left_idx >= len(left) and right_idx < len(right):
            combined.append(right[right_idx])
            right_idx += 1
        else:
            if right[right_idx] <= left[left_idx]:
                combined.append(right[right_idx])
                right_idx += 1
            else:
                combined.append(left[left_idx])
                left_idx += 1

    return combined
