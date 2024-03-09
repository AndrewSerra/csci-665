__author__ = "Andrew Serra"
'''


Author: Andrew Serra
Date: 02/27/2024
'''
from math import atan2, degrees

def get_polar_ang(point1, point2):
    '''
    Returns polar angle between two points
    '''
    return atan2(point2[1]-point1[1], point2[0] - point1[0])


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


def find_right_triangles(points):
    
    if len(points) == 1:
        return points
    
    points = merge_sort(points, axis=0)
    groups = {}

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            polar = degrees(get_polar_ang(points[i], points[j]))
            
            if polar in groups:
                groups[polar].append((i, j))
            else:
                groups[polar] = [(i,j)]
    
    result_pairs_cnt = 0

    for angle1, v1 in groups.items():
        for angle2, v2 in groups.items():
            if abs(angle1 - angle2) == 90:
                for pair1 in v1:
                    for pair2 in v2:
                        if any(x in pair1 for x in pair2):
                            result_pairs_cnt += 1

    return result_pairs_cnt // 2



if __name__ == "__main__":
    try:
        num_items = int(input().strip())
        positions = []

        for i in range(num_items):
            pair = list(map(lambda x: int(x), input().strip().split()))
            positions.append(pair)

        num_triangles = find_right_triangles(positions)
        print(num_triangles)

    except Exception as e:
        print(f"Error running code: {e}")
