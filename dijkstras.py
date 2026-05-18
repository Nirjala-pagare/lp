import heapq

def dijkstra(graph, source, vertices):
    distance = [float('inf')] * vertices
    distance[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if current_distance > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distance


vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = [[] for i in range(vertices)]

print("Enter edges:")

for i in range(edges):
    u = int(input("Enter source vertex: "))
    v = int(input("Enter destination vertex: "))
    w = int(input("Enter weight: "))

    graph[u].append((v, w))
    graph[v].append((u, w))


source = int(input("Enter source vertex: "))

distances = dijkstra(graph, source, vertices)

print("\nShortest distances from source vertex", source)

for i in range(vertices):
    print("Vertex", i, "=", distances[i])