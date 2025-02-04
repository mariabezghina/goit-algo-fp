import heapq

def dijkstra(graph, start):

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue  

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Use

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5, 'E': 12},
    'C': {'D': 10, 'F': 3},
    'D': {'E': 2, 'F': 1},
    'E': {'F': 7},
    'F': {}  
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Найкоротші шляхи від вершини {start_node}:")
for vertex, distance in shortest_paths.items():
    print(f"До {vertex}: {distance}")
