#!/usr/bin/python3
from typing import Any

def insertion_sort(arr: list[Any]) -> list[Any]:
    
    for i in range(len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

