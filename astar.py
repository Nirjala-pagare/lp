from heapq import heappush, heappop

def display_graph(graph):
    print()
    for node in graph:
        print(f"{node} -> ", end="")
        for neighbour, cost in graph[node]:
            print(f"({neighbour},{cost})", end=" ")
        print()

def a_star(graph, heuristic, start, goal):
    priority_queue = []
    heappush(priority_queue, (heuristic[start], start))
    visited = set()

    g_cost = {}
    parent = {}

    g_cost[start] = 0
    parent[start] = None

    while priority_queue:
        current_f_cost, current_node = heappop(priority_queue)
        if current_node in visited:
            continue
        visited.add(current_node)
        print(f"Visited : {current_node}")

        if current_node == goal:
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("\nPath Found : ", end="")

            for node in path:
                print(node, end=" ")

            print(f"\nTotal Cost : {g_cost[goal]}")

            return

        for neighbour, cost in graph[current_node]:
            new_g_cost = g_cost[current_node] + cost
            f_cost = new_g_cost + heuristic[neighbour]

            if neighbour not in g_cost or new_g_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_g_cost
                parent[neighbour] = current_node

                heappush(priority_queue, (f_cost, neighbour))

    print("\nNo Path Found.")

def main():

    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('D', 3), ('E', 6)],
        'C': [('F', 5)],
        'D': [('G', 2)],
        'E': [('G', 1)],
        'F': [('G', 2)],
        'G': []
    }

    heuristic = {
        'A': 7,
        'B': 6,
        'C': 4,
        'D': 2,
        'E': 1,
        'F': 2,
        'G': 0
    }

    while True:

        print("\n1. Display Graph")
        print("2. Run A* Algorithm")
        print("3. Exit")

        choice = int(input("\nEnter your choice : "))

        if choice == 1:
            display_graph(graph)

        elif choice == 2:

            start = input("\nEnter Start Node : ").upper()

            goal = input("Enter Goal Node : ").upper()

            print("\nA* Traversal ---->\n")

            a_star(graph, heuristic, start, goal)

        elif choice == 3:
            print("\nProgram Terminated.")
            break

        else:
            print("\nEnter Valid Option.")

main()