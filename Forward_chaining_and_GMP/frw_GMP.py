import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Define the maze as a 2D grid (0: free path, 1: obstacle)
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0]
]
# Start and end positions
start = (0, 0)
end = (4, 5)

# Define possible moves (up, down, left, right)
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to check if a position is within the maze and valid (not an obstacle)
def is_valid_position(x, y, maze, visited):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0 and (x, y) not in visited

# Generalized Modus Ponens (GMP) inference function
def apply_gmp(current_position, directions, visited):
    # GMP logic: infer possible new positions based on current position and directions
    valid_moves = []
    x, y = current_position
    for dx, dy in directions:
        next_x, next_y = x + dx, y + dy
        if is_valid_position(next_x, next_y, maze, visited):
            valid_moves.append((next_x, next_y))
    return valid_moves

# Forward-chaining with GMP inference
def forward_chaining(maze, start, end):
    queue = deque([(start, [start])])  # Queue holds tuples of (current position, path taken)
    visited = set()
    visited.add(start)
    
    frames = []  # To store the frames for animation

    while queue:
        current_position, path = queue.popleft()
        x, y = current_position

        # Store the current state for the animation
        frames.append((current_position, path))

        # Check if we have reached the end
        if current_position == end:
            print("Path found:", path)
            print("____________________________________________________________")
            print("Number of steps:", len(path) - 1)
            return path, frames  # Return the path to the goal and frames for animation
        
        # Apply GMP to infer valid moves
        valid_moves = apply_gmp(current_position, directions, visited)
        for move in valid_moves:
            if move not in visited:
                visited.add(move)
                new_path = path + [move]
                queue.append((move, new_path))
                print(f"Applying GMP: Moving to {move}, Path so far: {new_path}")
    
    print("No path found.")
    return None, frames  # Return None if no path is found

# Function to plot the maze and animate the process
def animate_maze(maze, path, frames, start, end):
    fig, ax = plt.subplots(figsize=(6, 6))
    
    # Function to update the plot for each frame
    def update_frame(i):
        ax.clear()
        ax.imshow(maze, cmap='binary', origin='upper')  # Set origin='upper' for correct y-axis direction
        
        # Highlight the start and end points
        ax.scatter(start[1], start[0], color='green', s=100, label='Start')
        ax.scatter(end[1], end[0], color='red', s=100, label='End')

        # Highlight the path explored so far
        current_pos, current_path = frames[i]
        path_x = [p[1] for p in current_path]
        path_y = [p[0] for p in current_path]
        ax.plot(path_x, path_y, color='blue', linewidth=3, label='Path')

        # Add the grid and labels for each coordinate
        for row in range(len(maze)):
            for col in range(len(maze[0])):
                ax.text(col, row, f"({row},{col})", ha='center', va='center', color='gray', fontsize=8)
        
        ax.legend()
        ax.set_xticks(range(len(maze[0])))  # Set x-axis ticks
        ax.set_yticks(range(len(maze)))  # Set y-axis ticks
        ax.set_xticklabels(range(len(maze[0])))  # Set x-axis labels
        ax.set_yticklabels(range(len(maze)))  # Set y-axis labels
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title(f"Forward-Chaining with GMP")
        # ax.set_title(f"Step {i + 1}")

    # Create the animation
    ani = animation.FuncAnimation(fig, update_frame, frames=len(frames), interval=500, repeat=False)
    plt.show()

# Run the forward-chaining algorithm
path, frames = forward_chaining(maze, start, end)

# Display the result and animation
if path:
    print("Final path:", path)
    animate_maze(maze, path, frames, start, end)
else:
    print("Goal not reached.")
