def is_safe(graph, colors, vertex, color):
    for neighbor in range(len(graph)):
        if graph[vertex][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True


def graph_coloring(graph, m, colors, vertex):
    n = len(graph)

    if vertex == n:
        return True

    for color in range(1, m + 1):
        if is_safe(graph, colors, vertex, color):
            colors[vertex] = color

            if graph_coloring(graph, m, colors, vertex + 1):
                return True

            colors[vertex] = 0

    return False


def main():
    n = int(input("Enter number of vertices: "))
    m = int(input("Enter number of colors: "))

    graph = []

    print("\nEnter adjacency matrix:")

    for i in range(n):
        row = []
        for j in range(n):
            value = int(input(f"Enter graph[{i}][{j}]: "))
            row.append(value)
        graph.append(row)

    colors = [0] * n

    if graph_coloring(graph, m, colors, 0):
        print("\nSolution Exists")
        print("Color assigned to vertices:")

        for i in range(n):
            print("Vertex", i, "=", "Color", colors[i])
    else:
        print("\nNo Solution Exists")


main()