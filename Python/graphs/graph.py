# # iterative dfs
# def depth_first_search(graph, source):
#     stack = [source]
#     visited = set()
    
#     while (len(stack) > 0):
#         current = stack.pop()
        
#         if current not in visited:
#             print(current)
#             visited.add(current)
        
#             for neighbor in graph[current]:
#                 stack.append(neighbor)
            
# recursive dfs
def depth_first_search(graph, source):
   print(source)
   for neighbor in graph[source]:
       depth_first_search(graph, neighbor)


# bfs
def breadth_first_search(graph, source):
    queue = [source]
    while (len(queue) > 0):
        current = queue.pop(0)
        print(current)
        
        for neighbor in graph[current]:
            queue.append(neighbor)

if __name__ == "__main__":
    graph = {
    'a': ['c', 'b'],
    'b': 'd',
    'c': 'e',
    'd': 'f',
    'e': [],
    'f': []
    
}
    # depth_first_search(graph, 'a')
    
    breadth_first_search(graph, 'a')
    
    