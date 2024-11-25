'''

author: Andrew Serra
date: 04/22/2024
'''

# O(m+n)
def run_dfs_finish_times(adj):
    n = len(adj)

    seen = [False] * n
    fin_t = []

    def dfs(node_idx):
        seen[node_idx] = True

        for nb in adj[node_idx]:
            if not seen[nb]:
                dfs(nb)
        
        if node_idx not in fin_t:
            fin_t.append(node_idx)

    for i in range(n):
        if not seen[i]:
            dfs(i)
        
    return fin_t

# O(m+n)
def reverse_graph(adj):
    n = len(adj)
    rev = [[] for _ in range(n)]
    for i in range(n):
        for node in adj[i]:
            rev[node].append(i)
    return rev

def dfs(graph, node, seen=None):
    if seen is None:
        seen = set()
    seen.add(node)
    for n in graph[node]:
        if n not in seen:
            dfs(graph, n, seen)
    return seen


if __name__ == "__main__":
    try:
        n = int(input().strip())
        adjacency = []

        for _ in range(n):
            adj = list(map(lambda x: int(x), input().strip().split()))
            adjacency.append(adj[:-1])

        final_times = run_dfs_finish_times(adjacency)
        rev_graph = reverse_graph(adjacency)
        
        sccs = []
        seen = set()

        for node in reversed(final_times):
            if node not in seen:
                s = dfs(rev_graph, node)
                seen.update(s)
                sccs.append(s)

        print(len(sccs)-1)

    except Exception as e:
        print(e)
