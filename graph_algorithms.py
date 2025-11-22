from collections import defaultdict
import heapq

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)
        self.nodes = set()

    def add_edge(self, u, v, w):
        self.nodes.add(u)
        self.nodes.add(v)
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))

    # BFS
    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                for v, _ in self.adj_list[node]:
                    queue.append(v)
        return order

    # DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        order = [start]
        for v, _ in self.adj_list[start]:
            if v not in visited:
                order.extend(self.dfs(v, visited))
        return order

    # Dijkstra
    def dijkstra(self, start):
        dist = {node: float('inf') for node in self.nodes}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            for v, w in self.adj_list[node]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    # Kruskal (minimum spanning tree)
    def kruskal(self):
        edges = []
        for u in self.adj_list:
            for v, w in self.adj_list[u]:
                if (v, u, w) not in edges:
                    edges.append((u, v, w))
        edges.sort(key=lambda x: x[2])

        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for node in self.nodes:
            parent[node] = node

        mst = []
        for u, v, w in edges:
            if find(u) != find(v):
                mst.append((u, v, w))
                union(u, v)
        return mst
