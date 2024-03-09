def counting_inversions(data: list[int], start: int, end: int) -> tuple[int, list[int]]:
    if len(data) == 1:
        return 0, data
    
    mid_idx = (start + end) // 2
    left, right = _split_arr(data)

    inv_l, ml = counting_inversions(left, start, mid_idx)
    inv_r, mr = counting_inversions(right, mid_idx, end)

    inv_m, m = _merge_and_count(ml, mr)

    return inv_l + inv_r + inv_m, m

def _split_arr(arr: list[int]) -> tuple[list[int], list[int]]:
    mid = len(arr) // 2
    return arr[:mid], arr[mid:]

def _merge_and_count(left: list[int], right: list[int]) -> tuple[int, list[int]]:
    i, j, count = 0, 0, 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i
            j += 1

    merged += left[i:]
    merged += right[j:]

    return count, merged

def minimum_somersaults(arr: list[int]) -> int:
    n = len(arr)
    inversions, _ = counting_inversions(arr, 0, n)
    
    # The minimum number of somersaults is half of the total inversions
    return inversions // 2

# Input
n = int(input())
order = list(map(int, input().split()))

# Output
result = minimum_somersaults(order)
print(result)
