'''

author: Andrew Serra
date: 04/22/2024
'''

def run_dijkstra(n, graph, source, sink):
    # tuple - node, edge cost, parent, toll count
    queue = [(source, 0, None, 0)]
    queue_id = 0
    costs = { i: (None, i, 0) for i in range(n) } # cost, parent, toll count
    v = []

    while queue_id < len(queue):
        node, cost, parent, toll_cnt = queue[queue_id]
        v.append(node)
        if costs[node][0] is None:
            costs[node] = (cost, parent, toll_cnt)
        else:
            costs[node] = min(costs[node], (cost, parent, toll_cnt), key=lambda x: x[0])

        for neighbor, edge_cost, toll in graph[node]:
            if neighbor in v or (toll and toll_cnt == 2):
                continue
            queue.append((neighbor, cost+edge_cost, node, toll_cnt+toll))

        queue_id += 1
    
    return costs[sink]

if __name__ == "__main__":
    try:
        # number of nodes
        n = int(input().strip())
        # number of possible connections
        m = int(input().strip())
        # source point
        start_node = int(input().strip())
        # sink point
        end_node = int(input().strip())
        
        adjacency = {}

        for _ in range(m):
            _from, _to, _cost, _is_toll = list(map(lambda x: int(x), input().strip().split()))
            if _from not in adjacency:
                adjacency[_from] = [(_to, _cost, _is_toll)]
            else:
                adjacency[_from].append((_to, _cost, _is_toll))

            if _to not in adjacency:
                adjacency[_to] = [(_from, _cost, _is_toll)]
            else:
                adjacency[_to].append((_from, _cost, _is_toll))

        result = run_dijkstra(n, adjacency, start_node, end_node)

        if result[0] is None:
            print(-1)
        else:
            print(result[0])

    except Exception as e:
        print(e)
