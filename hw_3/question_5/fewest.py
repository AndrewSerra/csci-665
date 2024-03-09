__author__ = "Andrew Serra"
'''


Author: Andrew Serra
Date: 02/27/2024
'''

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def smallest_elems_sum_thresh_cnt(arr, c):
    quicksort(arr, 0, len(arr) - 1)

    current_sum = 0
    count = 0

    for i in range(len(arr) - 1, -1, -1):
        current_sum += arr[i]
        count += 1

        if current_sum > c:
            return count

    return count

if __name__ == "__main__":
    try:
        num_items = int(input().strip())
        thresh = int(input().strip())
        nums = list(map(lambda x: int(x), input().strip().split()))

        num_elements = smallest_elems_sum_thresh_cnt(nums, thresh)
        print(num_elements)

    except Exception as e:
        print(f"Error running code: {e}")
