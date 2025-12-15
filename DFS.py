graph = {}
n = int(input())
for _ in range(n):
    node = input().strip()
    graph[node] = input().split()

visited = set()
def dfs(s):
    if s not in visited:
        print(s, end=" ")
        visited.add(s)
        for x in graph.get(s, []):
            dfs(x)

dfs(input().strip())

