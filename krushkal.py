def find(parent, node):
    if parent[node] == node:
        return node
    return find(parent, parent[node])

def union(parent, u, v):
    root_u = find(parent, u)
    root_v = find(parent, v)

    parent[root_v] = root_u

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])

    parent = []

    for i in range(vertices):
        parent.append(i)

    mst = []
    total_cost = 0

    for edge in edges:
        u = edge[0]
        v = edge[1]
        w = edge[2]

        if find(parent, u) != find(parent, v):
            mst.append((u, v, w))
            total_cost = total_cost + w
            union(parent, u, v)

    print("\nEdges in Minimum Spanning Tree:")

    for edge in mst:
        print(edge[0], "-", edge[1], "=", edge[2])

    print("Minimum Cost =", total_cost)

vertices = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    print("\nEnter Edge", i + 1)

    u = int(input("Enter source vertex: "))
    v = int(input("Enter destination vertex: "))
    w = int(input("Enter weight: "))

    edges.append((u, v, w))

kruskal(vertices, edges)