__author__ = "Andrew Serra"
'''
A program that groups duplicate data together in
minimal number of adjacent swaps.

Author: Andrew Serra
Date: 02/12/2024
'''

def _split_arr(data: list[int]) -> tuple[list[int], list[int]]:
    '''
    Splits a list into two parts from the middle.

    @param data The list two split into two parts

    @returns A tuple containing the left half and the right half of the input
    '''
    mid = len(data) // 2
    return data[:mid], data[mid:]

def _merge_and_count(left: list[int], right: list[int]) -> tuple[int, list[int]]:
    '''
    Merges two lists and counts inversions needed.

    @param left  Left half of the data
    @param right Right half of the data

    @returns A tuple containing the number of inversions and the merged list
    '''
    li, ri = 0, 0
    inversions = 0
    _merge, dup = [], []

    while li < len(left) or ri < len(right):
        if li < len(left) and ri < len(right):
            if left[li] in right:
                index = right.index(left[li])

                # distance to the edge
                if (len(right) - 1 - index) > li:
                    _merge.append(right[index])
                    _merge.append(left[li])
                    inversions += (len(left) + index - li - 1 )
                    right = right[:index] + right[index+1:]
                    left = left[:li] + left[li+1:]
                else:
                    dup.append(left[li])
                    inversions += (len(left) + index - li - 1)
                    left = left[:li] + left[li+1:]
            else:
                _merge.append(left[li])
                li += 1
        else:
            if right[ri] in dup:
                _merge.extend([right[ri], right[ri]])
            else:
                _merge.append(right[ri])
            ri += 1
    return inversions, _merge


def counting_inversions(data: list[int], start: int, end: int) -> tuple[int, list[int]]:
    '''
    A recursive function counting the minimum number of inversions 
    required to group gymnasts.

    @param data  The data list to group
    @param start The starting index
    @param end   The ending index
    '''
    if len(data) == 1:
        return 0, data
    
    mid_idx = (end - start) // 2
    left, right = _split_arr(data)

    inv_l, ml = counting_inversions(left, start, mid_idx)
    inv_r, mr = counting_inversions(right, mid_idx, end)

    inv_m, m = _merge_and_count(ml, mr)
    return inv_l + inv_r + inv_m, m


if __name__ == "__main__":
    try:
        num_gymnasts = int(input().strip())
        order = list(map(lambda x: int(x), input().strip().split()))
        inv, m = counting_inversions(order, 0, len(order))
        print(inv) 

    except ValueError as e:
        print(f"Error converting values to integers: {e}")
