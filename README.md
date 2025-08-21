# AI Maze Navigation: Bidirectional Search & Logical Inference


<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/3b0e2e65-5777-4393-9d09-8c1cff8b8644" />

<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/1c6de82b-c8cd-44b4-88c1-5b261c1760ac" />


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

## 📊 Results

**Bidirectional Search Results**

<img width="909" height="939" alt="image" src="https://github.com/user-attachments/assets/e81a1719-892f-4c70-b445-c088151f9cdf" />

    Path Found: [(0,0), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (2,5), (3,5), (4,5)]
    Total Cost: 9 steps
    Nodes Explored: Significantly fewer than traditional BFS

**Forward-Chaining Results**


    Path Found: [(0,0), (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (2,5), (3,5), (4,5)]
    Total Steps: 9
    Logical Rules Applied: Successfully navigated using GMP inference

## 🎥 Demonstrations

**Bidirectional Search Visualization**

![1 - Made with Clipchamp (2)](https://github.com/user-attachments/assets/1155562c-fe85-42d2-ac3b-8b0536ead9ff)


The algorithm searches from both ends simultaneously, meeting in the middle


**Forward-Chaining Process**

![Untitled video - Made with Clipchamp](https://github.com/user-attachments/assets/b7b2d28f-3630-48a3-acb3-e048eeb0df34)


Logical inference applied step-by-step to determine valid moves




**🧠 Algorithm Details**

**Bidirectional Search**

    Time Complexity: O(b^(d/2)) where b is branching factor, d is depth
    Space Complexity: O(b^(d/2))
    Optimality: Guarantees shortest path
    Advantage: Reduces search space exponentially

**Forward-Chaining with GMP**

    Reasoning Type: Goal-driven logical inference
    Knowledge Representation: First-Order Logic (FOL)
    Inference Method: Generalized Modus Ponens
    Advantage: Systematic, explainable decision making

**📈 Performance Comparison**

| **Algorithm**        | **Path Length** | **Nodes Explored** | **Time Complexity** | **Memory Usage** |
| -------------------- | --------------- | ------------------ | ------------------- | ---------------- |
| Bidirectional Search | 9               | \~15               | O(b^(d/2))          | Medium           |
| Forward Chaining     | 9               | \~25               | O(rules × facts)    | Low              |






## **👨‍💻 Author**
### ***Bhargavkumar Panchal***

GitHub: @bbhargavpanchal

LinkedIn: https://www.linkedin.com/in/bhargavpanchall/




📞 Support

Email: bhargavpanchal5151@gmail.com


⭐ If you find this project useful, please consider giving it a star!
