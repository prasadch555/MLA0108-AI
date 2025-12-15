import heapq

# Graph with edge weights
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'F': 1, 'E': 1},
    'E': {'F': 2},
    'F': {}
}

# Simple heuristic values (straight-line guess)
h = {
    'A': 6,
    'B': 5,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 0
}

def a_star(start, goal):
    pq = []                      # priority queue
    heapq.heappush(pq, (0, start))
    
    parent = {start: None}
    g_cost = {start: 0}
    
    print("Node Expansion Order:")
    
    while pq:
        f, node = heapq.heappop(pq)
        print(node, end=" ")
        
        if node == goal:
            break
        
        for nei, w in graph[node].items():
            new_cost = g_cost[node] + w
            if nei not in g_cost or new_cost < g_cost[nei]:
                g_cost[nei] = new_cost
                f_cost = new_cost + h[nei]
                heapq.heappush(pq, (f_cost, nei))
                parent[nei] = node
    
    # Reconstruct path
    path = []
    n = goal
    while n is not None:
        path.append(n)
        n = parent[n]
    path.reverse()
    
    print("\n\nOptimal Path:", path)
    print("Total Cost:", g_cost[goal])


# Run A*
a_star('A', 'F')
