import heapq

# Goal state
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Convert 2D matrix to tuple for storing in set/dictionary
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Manhattan Distance Heuristic
def heuristic(state):
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i][j]

            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3

                distance += abs(i - goal_x) + abs(j - goal_y)

    return distance

# Find position of blank tile
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate next possible states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dx, dy in moves:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]

            neighbors.append(new_state)

    return neighbors

# Print puzzle state
def print_state(state):
    for row in state:
        print(row)
    print()

# A* Algorithm
def a_star(start):
    priority_queue = []
    visited = set()

    g = 0
    h = heuristic(start)
    f = g + h

    heapq.heappush(priority_queue, (f, g, start, []))

    while priority_queue:
        f, g, current, path = heapq.heappop(priority_queue)

        if to_tuple(current) in visited:
            continue

        visited.add(to_tuple(current))

        new_path = path + [current]

        if current == goal:
            print("Goal State Reached!")
            print("Number of moves:", g)
            print("\nSolution Path:\n")

            for step in new_path:
                print_state(step)

            return

        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) not in visited:
                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h

                heapq.heappush(priority_queue, (new_f, new_g, neighbor, new_path))

    print("No solution found.")


# Main Program
start = []

print("Enter initial 8-puzzle state:")
print("Use 0 for blank space")

for i in range(3):
    row = list(map(int, input(f"Enter row {i + 1}: ").split()))
    start.append(row)

print("\nInitial State:")
print_state(start)

a_star(start)