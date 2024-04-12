'''
Author: Andrew Serra
Date: 04/09/2024
'''

def could_pick_half(n, cards):
    adjacency_list = {i: [] for i in range(1, n+1)}

    for card in cards:
        n1, n2 = card
        adjacency_list[n1].append(n2)
        adjacency_list[n2].append(n1)

    q = [(1,0)]
    proc_id = 0
    visited = []

    while proc_id < len(q):
        id, level = q[proc_id]
        proc_id += 1
        visited.append(id)
        edges = adjacency_list[id]

        count = 0

        for edge in edges:
            if edge not in visited:
                q.append((edge, level+1))
                count += 1

        if count == 0 and level % 2 == 1:
            return "NO"

    return "YES"


if __name__ == "__main__":
    try:
        # number of cards
        n = int(input().strip())
        # every card and its numeric values
        cards = []
        for _ in range(n):
            cards.append(tuple(map(int, input().strip().split())))

        print(could_pick_half(n, cards))

    except ValueError as e:
        print(e)
