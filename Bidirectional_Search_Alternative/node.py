class Node:
    def __init__(self, position=None, parent=None):
        self.position = position  # Tuple representing the (row, column) of the node
        self.parent = parent  # Parent node for path tracking
        self._g = 0  # Cost from the start node (g-value)
        self._h = 0  # Heuristic estimate to the goal (h-value)
        self.f = 0  # Total cost (f = g + h)

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g = value

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, value):
        self._h = value

    @property
    def f(self):
        return self.g + self.h

    @f.setter
    def f(self, value):
        self._f = value

    def update_costs(self, predecessor_node, goal_node):
        """
        Update g, h, and f values based on the predecessor and goal.
        g: distance from start to this node
        h: heuristic distance from this node to goal
        f: total cost, f = g + h
        """
        self.g = predecessor_node.g + 1  # Add the cost to reach this node from predecessor
        self.h = ((self.position[0] - goal_node.position[0]) ** 2) + ((self.position[1] - goal_node.position[1]) ** 2)
        self.f = self.g + self.h  # Update the f-value as sum of g and h

    def __lt__(self, other):
        """
        Comparison method to enable sorting nodes by f-value.
        Nodes with lower f values come first (used for priority queues).
        """
        return self.f < other.f

    def __repr__(self):
        return f"Node(position={self.position}, g={self.g}, h={self.h}, f={self.f})"

    def get_path(self):
        """
        Get the path from the start node to this node by traversing parent pointers.
        """
        path = []
        current_node = self
        while current_node is not None:
            path.append(current_node.position)
            current_node = current_node.parent
        return path[::-1]  # Return reversed path, from start to goal

    def __eq__(self, other):
        """ Override equality to compare Node objects based on position. """
        return self.position == other.position
