from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}
    
    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []
    
    def add_edge(self, u, v):
        self.add_vertex(v)
        self.add_vertex(u)
        self.adj[v].append(u)
        self.adj[u].append(v)
    
    # DFS
    def DFS_R(self, start = 1):
        visited = set()
        result = []
        self._DFS_R(visited, result, start)
        return result
    
    def _DFS_R(self, visited, result, v):
        # print(visited)
        visited.add(v)
        result.append(v)
        for n in self.adj[v]:
            if n not in visited:
                self._DFS_R(visited, result, n)
        
    def DFS_I(self, start = 1):
        visited = set()
        children = [start]
        result = []

        while children:
            v = children.pop()
            if v not in visited:
                visited.add(v)
                result.append(v)

                for n in self.adj[v][::-1]:
                    if n not in visited:
                        children.append(n)
        return result


    # BFS
    def BFS(self, start = 1):
        visited = set([start])
        queue = [start]
        result = []

        while queue:
            v = queue.pop(0)
            result.append(v)
            
            for n in self.adj[v]:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        return result


if __name__ == "__main__":
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    print(g.DFS_R()) # DFS recursive
    print(g.DFS_I()) # DFS iteration
    print(g.BFS()) # BFS