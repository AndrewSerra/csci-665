'''

author: Andrew Serra
date: 04/22/2024
'''

def filter_edges(edges, sec_levels):
    e, r = [], []
    for sc, sk, c in edges:
        if sec_levels[sc] >= sec_levels[sk]:
            e.append((sc, sk, c))
        else:
            r.append((sc, sk, c))
    return e, r

def run_kruskal(n, edges):
    boss = [i for i in range(n)]
    size = [1 for _ in range(n)]
    _set = [[i] for i in range(n)]

    _t = []

    def union(u, v):
        if size[boss[u]] >= size[boss[v]]:
            _set[boss[u]].extend(_set[boss[v]])
            size[boss[u]] += size[boss[v]]

            for z in _set[boss[v]]:
                boss[z] = boss[u]
        else:
            _set[boss[v]].extend(_set[boss[u]])
            size[boss[v]] += size[boss[u]]

            for z in _set[boss[u]]:
                boss[z] = boss[v]

    for edge in edges:
        if boss[edge[0]] != boss[edge[1]]:
            _t.append(edge)
            union(edge[0], edge[1])

    return _t



if __name__ == "__main__":
    try:
        # number of computers
        n = int(input().strip())
        # number of possible connections
        m = int(input().strip())
        # security levels
        sec_levels = list(map(lambda x: int(x), input().strip().split()))

        adjacency = {}
        edges = []

        for _ in range(m):
            _from, _to, _cost = list(map(lambda x: int(x), input().strip().split()))
            edges.append((_from, _to, _cost))
            if _from not in adjacency:
                adjacency[_from] = [(_to, _cost)]
            else:
                adjacency[_from].append((_to, _cost))

            if _to not in adjacency:
                adjacency[_to] = [(_from, _cost)]
            else:
                adjacency[_to].append((_from, _cost))

        edges.sort(key=lambda x: x[2])

        while len(edges) >= n-1:
            tree = run_kruskal(n, edges)
            selected, rejected = filter_edges(tree, sec_levels)
            edges = [item for item in edges if item not in rejected]

            if len(rejected) == 0:
                break

        if len(edges) != n-1:
            print(-1)
        else:
            print(sum(map(lambda x: x[2], edges)))

    except Exception as e:
        print(e)
