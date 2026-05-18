import heapq

def prim(graph, vertices):
    visited = [False] * vertices
    mst = []
    total_cost = 0

    priority_queue = [(0, 0, -1)]

    while priority_queue:
        weight, node, parent = heapq.heappop(priority_queue)

        if visited[node]:
            continue

        visited[node] = True
        total_cost = total_cost + weight

        if parent != -1:
            mst.append((parent, node, weight))

        for neighbor, edge_weight in graph[node]:
            if visited[neighbor] == False:
                heapq.heappush(priority_queue, (edge_weight, neighbor, node))

    print("\nEdges in Prim's MST:")

    for edge in mst:
        print(edge[0], "-", edge[1], ":", edge[2])

    print("Minimum Cost:", total_cost)

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = []

for i in range(vertices):
    graph.append([])

for i in range(edges):
    print("\nEnter Edge", i + 1)

    u = int(input("Enter source vertex: "))
    v = int(input("Enter destination vertex: "))
    w = int(input("Enter weight: "))

    graph[u].append((v, w))
    graph[v].append((u, w))

prim(graph, vertices)