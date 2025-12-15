 from collections import deque

n = int(input("Enter number of edges: "))
g = {}

# Read graph edges
for _ in range(n):
    a, b = input().split()
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)

# Start node
s = input("Enter starting node: ")

# BFS
v = set()
q = deque([s])

while q:
    x = q.popleft()
    

    if x in v:
        continue

    v.add(x)
    print(x, end=' ')

    for y in g[x]:
        q.append(y)
