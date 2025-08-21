import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Define the grid and start/goal points
grid = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]
]
start = (0, 0)
goal = (4, 5)

# Directions for moving in the grid (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Perform bidirectional search
def bidirectional_search(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0

    def bfs(start, goal):
        visited = []
        parent = {}
        queue = deque([start])
        visited.append(start)
        parent[start] = None
        while queue:
            node = queue.popleft()
            if node == goal:
                break
            for dx, dy in directions:
                nx, ny = node[0] + dx, node[1] + dy
                if valid_move(nx, ny) and (nx, ny) not in visited:
                    visited.append((nx, ny))
                    parent[(nx, ny)] = node
                    queue.append((nx, ny))
        return visited, parent

    # Bidirectional BFS
    visited_start, parent_start = bfs(start, goal)
    visited_goal, parent_goal = bfs(goal, start)

    # Reconstruct the path
    def reconstruct_path(parent_start, parent_goal, meeting_point):
        path = []
        node = meeting_point
        while node is not None:
            path.append(node)
            node = parent_start.get(node)
        path = path[::-1]
        node = parent_goal.get(meeting_point)
        while node is not None:
            path.append(node)
            node = parent_goal.get(node)
        return path

    # Find the meeting point
    meeting_point = None
    for node in visited_start:
        if node in visited_goal:
            meeting_point = node
            break

    path = []
    if meeting_point:
        path = reconstruct_path(parent_start, parent_goal, meeting_point)

    return path, visited_start, visited_goal

# Visualization using matplotlib
fig, ax = plt.subplots(figsize=(8, 8))

# Create an image for the grid
grid_image = [[1 if cell == 1 else 0 for cell in row] for row in grid]
ax.imshow(grid_image, cmap='binary', interpolation='nearest')

# Get the path and visited nodes
path, visited_nodes_start, visited_nodes_goal = bidirectional_search(grid, start, goal)

# Animation update function
def update(frame):
    ax.clear()
    ax.imshow(grid_image, cmap='binary', interpolation='nearest')

    # Plot visited nodes from both searches
    if frame < len(visited_nodes_start):
        start_x, start_y = zip(*visited_nodes_start[:frame+1])
        ax.scatter(start_y, start_x, color='orange', s=300, label='Visited (Forward)', zorder=3)

    if frame < len(visited_nodes_goal):
        goal_x, goal_y = zip(*visited_nodes_goal[:frame+1])
        ax.scatter(goal_y, goal_x, color='purple', s=300, label='Visited (Backward)', zorder=3)

    # Plot the path
    if path and frame < len(path):
        path_x, path_y = zip(*path[:frame+1])
        ax.plot(path_y, path_x, marker='o', color='blue', markersize=10, linestyle='-', linewidth=2)

    # Mark start and goal positions
    if path:
        ax.scatter(path_y[0], path_x[0], color='green', s=300, label='Start', zorder=5)
        ax.scatter(path_y[-1], path_x[-1], color='red', s=300, label='Goal', zorder=5)

    # Label each grid cell
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            ax.text(j, i, f'({i},{j})', ha='center', va='center', fontsize=8, color='lightgray', zorder=0)

    # Display total cost
    total_cost = len(path) - 1 if path else "N/A"
    ax.text(0.5, 1.05, f"Total cost: {total_cost}", ha='center', va='bottom', fontsize=12, color='blue', transform=ax.transAxes)

    # Set the title and set Y-axis in ascending order
    ax.set_title("Bidirectional Search Visualization")
    ax.set_yticks(range(5))
    ax.set_yticklabels(range(5))  # Label Y-axis as ascending from 0 to 4
    ax.set_xticks(range(len(grid[0])))
    ax.set_xticklabels(range(len(grid[0])))

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=max(len(visited_nodes_start), len(visited_nodes_goal)), interval=500, repeat=False)

# Adjust layout for better visualization
plt.tight_layout()

# Show the animation
plt.show()

# Print the path and total cost
print("Path found:", path)
print("Total cost of the path:", len(path) - 1 if path else "N/A")
