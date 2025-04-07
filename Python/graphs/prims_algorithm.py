import heapq

def prim(graph, start):
    visited = set()
    mst = []
    queue = []
    cost = 0
    
    
    visited.add(start)
    # adds the neighbors of the starting node
    for neighbor, weight in graph[start]:
        heapq.heappush(queue, (weight, start, neighbor))
        
    while queue:
        weight, u, v = heapq.heappop(queue) # gets the smaller edge in the queue
        
        if v not in visited:
            # adds the edge in the mst and calcs the current weight of the tree
            cost += weight
            visited.add(v)
            mst.append((u, v, weight)) 
            
            for neighbor, n_weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(queue, (n_weight, v, neighbor))
                    
    return mst, cost


if __name__ == "__main__":
    graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}
    
    mst, cost = prim(graph, 'A')
    print(f"MST: {mst}")
    print(f"Cost: {cost}")