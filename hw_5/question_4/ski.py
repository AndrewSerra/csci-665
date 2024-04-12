'''
Author: Andrew Serra
Date: 04/09/2024
'''

def dfs(matrix, row, col, visited, stack):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    visited[row][col] = True

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and not visited[new_row][new_col]:
            if matrix[new_row][new_col] > matrix[row][col]:
                dfs(matrix, new_row, new_col, visited, stack)
    
    stack.append((row, col))

def topological_order(matrix):
    stack = []
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if not visited[row][col]:
                dfs(matrix, row, col, visited, stack)
    
    return stack[::-1]

def longest_path(matrix):
    topological_ordering = topological_order(matrix)

    S = [0] * len(topological_ordering)

    for j, (row, col) in enumerate(topological_ordering):
        max_length = 0
        for i in range(j):
            if matrix[topological_ordering[i][0]][topological_ordering[i][1]] < matrix[row][col]:
                max_length = max(max_length, S[i])
        S[j] = max_length + 1

    return max(S)

if __name__ == "__main__": 
    try:
        # the number of rows
        m = int(input().strip())
        # the number of columns
        n = int(input().strip())

        graph = []

        for _ in range(m):
            r = list(map(lambda x: int(x), input().strip().split()))
            graph.append(r)

        print(longest_path(graph))

    except ValueError as e:
        print(e)
