def largest_component(graph):
    visited = set()
    longest = 0
    
    for node in graph:
        size = explore_size(graph, node, visited)
        if size > longest: 
            longest = size
    
    return longest


def explore_size(graph, node, visited):
    if node in visited: return 0
    
    visited.add(node)
    size = 1
    
    for neighbor in graph[node]:
        size += explore_size(graph, neighbor, visited)
    
    return size

if __name__ == "__main__":
    
    print(largest_component({
        '0': ['8', '1', '5'],
        '1': '0',
        '5': ['0', '8'],
        '8': ['0', '5'],
        '2': ['3', '4'],
        '3': ['2', '4'],
        '4': ['3', '2']
    })) # -> 4