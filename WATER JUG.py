from collections import deque

cap = (4, 3)  # Jug capacities: 4-gallon, 3-gallon

def bfs():
    visited = set()
    queue = deque([((0, 0), [])])
    
    while queue:
        (j1, j2), path = queue.popleft()
        if j1 == 2:  # Goal: 2 gallons in 4-gallon jug
            return path + [(j1, j2)]
        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))
        moves = [
            (cap[0], j2), (j1, cap[1]), (0, j2), (j1, 0),
            (j1 - min(j1, cap[1]-j2), j2 + min(j1, cap[1]-j2)),
            (j1 + min(j2, cap[0]-j1), j2 - min(j2, cap[0]-j1))
        ]
        for m in moves:
            if m not in visited:
                queue.append((m, path + [(j1, j2)]))

# Run BFS and print solution
solution = bfs()
print("\nSolution Steps (4-gallon jug, 3-gallon jug):\n")
for step in solution:
    print(step)
