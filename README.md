# AI Maze Navigation: Bidirectional Search & Logical Inference



## 📋 Overview

This project implements two distinct AI approaches for solving maze navigation problems:

1. **Bidirectional Search Algorithm** - A state-space search technique that searches simultaneously from start and goal nodes
2. **Forward-Chaining with Generalized Modus Ponens (GMP)** - A knowledge-based approach using logical inference

Both algorithms are applied to a 5×6 grid maze to find the optimal path from start (0,0) to goal (4,5) while avoiding obstacles.

## 🎯 Features

- **Bidirectional Search Implementation**
  - Simultaneous search from start and goal positions
  - Efficient path reconstruction at meeting point
  - Reduced search space compared to traditional algorithms
  - Real-time visualization with matplotlib

- **Knowledge-Based Logical Inference**
  - Forward-chaining reasoning with GMP
  - First-Order Logic (FOL) representation
  - Systematic logical rule application
  - Step-by-step decision tracking

- **Interactive Visualizations**
  - Animated pathfinding process
  - Color-coded exploration (orange: forward, purple: backward)
  - Grid coordinate labeling
  - Path cost calculation

## 🗂️ Project Structure

    ai-maze-navigation-algorithms/
    │
    ├── src/
    │   ├── Bidirectional_search.py    # Bidirectional search implementation
    │   ├── frw_GMP.py                 # Forward-chaining with GMP
    │   └── node.py                    # Node class for pathfinding
    │
    ├── docs/
    │   └── project_report.pdf         # Complete project documentation
    │
    ├── assets/
    │   ├── images/                    # Screenshots and diagrams
    │   │   ├── bidirectional_viz.png
    │   │   ├── forward_chaining_viz.png
    │   │   └── maze_grid.png
    │   │
    │   └── videos/                    # Algorithm demonstrations
    │       ├── bidirectional_demo.mp4
    │       └── forward_chaining_demo.mp4
    │
    ├── results/
    │   ├── bidirectional_output.txt
    │   └── forward_chaining_output.txt
    │
    ├── README.md
    ├── requirements.txt
    └── LICENSE

