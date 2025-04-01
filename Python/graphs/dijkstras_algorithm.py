import heapq

def dijkstras(edges, start):
    validate_graph(edges)
    graph = build_graph_w(edges)
    
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        curr_dist, curr_node = heapq.heappop(priority_queue)
        
        # verifies if the current distance is larger than the shortest distance registered for the node
        if curr_dist > shortest_paths[curr_node]:
            continue
        
        for neighbor, weight in graph[curr_node]:
            dist = curr_dist + weight
            
            if dist < shortest_paths[neighbor]:
                shortest_paths[neighbor] = dist
                heapq.heappush(priority_queue, (dist, neighbor))
            
    return shortest_paths
    
    
def build_graph_w(edges):
    graph = {}
    
    for edge in edges:
        [a, b, c] = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    return graph

def validate_graph(edges):
    for node1, node2, weight in edges:
        if weight < 0:
            raise ValueError("Negative edge detected, not suitable for dijkstras algorithm")

if __name__ == "__main__":
    edges = [
    ('A', 'B', 4),
    ('A', 'C', 1),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 2),
    ('D', 'F', 6),
    ('E', 'F', 3)
    ]
    
    print(dijkstras(edges, 'A'))