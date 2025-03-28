def shortest_path(edges, node_a, node_b):
    graph = build_graph(edges)
    visited = set([node_a])
    queue = [[node_a, 0]]
    
    while len(queue) > 0:
        [node, distance] = queue.pop(0)
        
        if node == node_b: return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, distance + 1])
                
    return -1

def build_graph(edges):
    graph = {}
    
    for edge in edges:
        [a, b] = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

if __name__ == "__main__":
        edges = [
        ['w', 'x'],
        ['x', 'y'],
        ['z', 'y'],
        ['z', 'v'],
        ['w', 'v']
    ]
        
        print(shortest_path(edges, 'w', 'z')) 