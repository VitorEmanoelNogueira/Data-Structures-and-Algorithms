class DisjointSet:
    def __init__(self, n):
        # Each element is initially its own parent
        self.parent = list(range(n))
        self.rank = [0] * n 
        
    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]   
    
    def union(self, x, y):
        # find the sets parents
        p_x = self.find(x)
        p_y = self.find(y)
        
        
        if p_x == p_y:
            return # already in the same set
        
        # Union by rank
        if self.rank[p_x] < self.rank[p_y]:
            self.parent[p_x] = p_y
        elif self.rank[p_x] > self.rank[p_y]:
            self.parent[p_y] = p_x
        else:
            self.parent[p_y] = p_x
            self.rank[p_x] += 1
            
            
def kruskal(graph):
    edges = []
    for vertex, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (neighbor, vertex, weight) not in edges:
                edges.append((vertex, neighbor, weight))
                
    edges.sort(key=lambda edge: (edge[2], edge[0], edge[1]))
    
    vertices = list(graph.keys())
    vertex_to_index = {v: i for i, v in enumerate(vertices)}
    disjoint_set = DisjointSet(len(vertices))
    
    mst = []
    for u, v, weight in edges:
        root_u = disjoint_set.find(vertex_to_index[u])
        root_v = disjoint_set.find(vertex_to_index[v])
        
        if root_u != root_v:
            mst.append((u, v, weight))
            disjoint_set.union(root_u, root_v)
    
    return mst
    
    
if __name__ == "__main__":
    graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

    mst = kruskal(graph)
    print(mst)
    
