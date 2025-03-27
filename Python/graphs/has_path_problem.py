# dfs
def has_path_dfs(graph, src, dst):
    if src == dst:
        return True
    
    for neighbor in graph[src]:
        if (has_path_dfs(graph, neighbor, dst) == True):
            return True
    
    return False

# bfs
def has_path_bfs(graph, src, dst):
    queue = [src]
    
    while (len(queue) > 0):
        current = queue.pop(0)
        
        if current == dst:
            return True
        
        for neighbor in graph[current]:
            queue.append(neighbor)
    
    return False

if __name__ == "__main__":
    graph = {
        'f': ['g', 'i'],
        'g': 'h',
        'h': [],
        'i': ['g', 'k'],
        'j': 'i',
        'k': []
    }
    
    print(has_path_dfs(graph, 'f', 'k'))
    print(has_path_bfs(graph, 'f', 'j'))
    