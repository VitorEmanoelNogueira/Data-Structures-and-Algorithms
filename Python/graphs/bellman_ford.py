def bellman_ford(graph, start):
    dist = {node: float('inf') for node in graph}
    predecessors = {node: None for node in graph}
    dist[start] = 0
    
    # relaxing edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
                    predecessors[neighbor] = node
    
    # verifying negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if dist[node] + weight < dist[neighbor]:
                raise ValueError("The graph contains a negative weight cycle")
    
    return dist, predecessors
    

def reconstruct_path(predecessors, start, end):
    path = []
    curr = end
    
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    path.reverse()
    
    if path [0] == start:
        return path
    else:
        return f"No acessible path from {start} to {end}"
    
    
if __name__ == "__main__":
    graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'D': 2, 'E': 2, 'C': 5},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'B': 2, 'E': 1},
    'E': {'B': 2, 'D': 1, 'C': 5},
    'F': {'G': 3},
    'G': {'F': 3}
    }
    
    shortest_path, predecessors = bellman_ford(graph, 'A')
    print(shortest_path)
    print(predecessors)
    print(reconstruct_path(predecessors, 'A', 'E'))