__author__ = "Andrew Serra"
'''
A program that find the maximum number
of points that are evenly spaced either in a 
column or a row.

Author: Andrew Serra
Date: 02/12/2024
'''
 
def find_max_iteration(data: list[list[int]]) -> int:
    '''
    Checks each point on the same row or the same column to
    determine if they are evenly spaced.

    @param data List of lists containing indexes of items on the same line

    @returns The maximum number of points spaced evenly
    '''
    max_count = 0

    for line in data:
        l = len(line)

        if l <= 2 and max_count < l:
            max_count = l
        elif len(line) > 2:
            mi, ma = min(line), max(line)
            diff = (ma - mi) // l
            
            for i in range(len(line)):
                if mi > line[i]:
                    mi = line[i]
                if ma < line[i]:
                    ma = line[i]

            satisfied = True
            for num in line:
                if not (ma == num or mi == num or \
                        ((num + diff in line) and (num - diff in line))):
                    satisfied = False
            
            if satisfied and max_count < l:
                max_count = l
                
    return max_count


def find_max_spaced_points(size: int, points: list[tuple[int,int]]) -> int:
    '''
    Find the maximum number of points that are evenly spaced
    either in a column or a row.

    @param size   Size of the number of points
    @param points The list of points as tuples (row, col)

    @returns Maximum number of points
    '''
    rows = [[] for _ in range(size)]
    cols = [[] for _ in range(size)]

    for i in range(len(points)):
        row, col = points[i]

        rows[row].append(col)
        cols[col].append(row)

    return max(find_max_iteration(rows), find_max_iteration(cols))

if __name__ == "__main__":
    try:
        num_items = int(input().strip())
        positions = []

        for i in range(num_items):
            pair = tuple(map(lambda x: int(x), input().strip().split()))
            positions.append(pair)

        print(find_max_spaced_points(num_items, positions))
    except ValueError as e:
        print(f"Error converting values to integers: {e}")
