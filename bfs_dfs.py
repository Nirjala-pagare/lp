from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()

        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print()

def dfs(graph, node, visited):
    
    visited.add(node)

    print(node, end=" ")

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def display_graph(graph):
    print("\nAdjacency List:")

    for node in graph:
        print(node, "->", end=" ")

        for neighbour in graph[node]:
            print(neighbour, end=" ")

        print()

def main():
    vertices = int(input("Enter number of vertices: "))
    edges = int(input("Enter number of edges: "))

    graph = {}

    for i in range(1, vertices + 1):
        graph[i] = []

    print("Enter edges:")

    for i in range(edges):
        u = int(input("Enter source vertex: "))
        v = int(input("Enter destination vertex: "))

        graph[u].append(v)
        graph[v].append(u)

    start_node = int(input("Enter starting vertex: "))

    while True:
        print("\n1. Display Graph")
        print("2. BFS")
        print("3. DFS")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_graph(graph)

        elif choice == 2:
            print("\nBFS Traversal:")
            bfs(graph, start_node)

        elif choice == 3:
            visited = set()

            print("\nDFS Traversal:")
            dfs(graph, start_node, visited)

            print()

        elif choice == 4:
            break

        else:
            print("Invalid Choice")

main()