__author__ = "Andrew Serra"
'''


Author: Andrew Serra
Date: 03/22/2024
'''

def _split_arr(arr, rec_f):
    mid = len(arr) // 2
    return rec_f(arr[:mid]), rec_f(arr[mid:])

# Axis is for elements grouped in a list
def merge_sort(arr, axis=None):

    if len(arr) <= 1:
        return arr
    
    left, right = _split_arr(arr, merge_sort)

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
            if axis is None:
                if right[right_idx] <= left[left_idx]:
                    combined.append(right[right_idx])
                    right_idx += 1
                else:
                    combined.append(left[left_idx])
                    left_idx += 1
            else:
                if right[right_idx][axis] <= left[left_idx][axis]:
                    combined.append(right[right_idx])
                    right_idx += 1
                else:
                    combined.append(left[left_idx])
                    left_idx += 1

    return combined

def getClosest(val1, val2, target, m):
 
    if (target - val1[1] >= val2[1] - target):
        return val2, m
    else:
        return val1, m - 1
    
# find the next job which applies to 
def bin_search_next_avail_et(jobs, target_time):
    l, r = 0, len(jobs)
    while l <= r:
        mid = l + (r - l) // 2

        if jobs[mid][2] == target_time:
            return mid
        elif jobs[mid][2] < target_time:
            l = mid + 1
        else:
            r = mid - 1
 
    mid = l + (r - l) // 2
    return mid - 1

def find_max_job_count(jobs):
    # sort by end time of jobs
    jobs_sorted = merge_sort(jobs, axis=1)
    job_cnt = 0
    print(jobs_sorted)
    while len(jobs_sorted):
        start, end, cid = jobs_sorted.pop()
        idx = len(jobs)
        while idx >= 0:
            idx = bin_search_next_avail_et(jobs[:-1], start)
            interval = jobs_sorted[idx]
            
            print(start, end, cid, " --- ", interval, idx)
            if interval[2] == abs(cid-1):
                jobs_sorted.pop(idx)
                break
            else:
                while idx >= 0:
                    if jobs_sorted[idx][2] == abs(cid-1):
                        break
                    idx -= 1

                if idx >= 0:
                    jobs_sorted.pop(idx)

        job_cnt += 1
    return job_cnt

if __name__ == "__main__":
    try:
        num_items = int(input().strip())
        items = []

        for i in range(num_items):
            item = list(map(lambda x: int(x), input().strip().split()))
            items.append(item)

        count = find_max_job_count(items)
        print(count)

    except ValueError as e:
        print(e)

