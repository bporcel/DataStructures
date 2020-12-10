BFS -> Breadth First Search (Looks level by level for the given node)
DFS -> Depth First Search (Looks every branch to the end for the given node)

**If you know a solution is not far from the root of the tree:**

- BFS

**If the tree is very deep and solutions are rare:**

- BFS 
- *Why not DFS:* As the node is really **deep** and solutions are **rare**, DFS can take an enormous time until it finds the answer

**If the tree is very wide:**

- DFS
- *Why not BFS:* With BFS we would need too much **memory**

**If solutions are frequent but located deep in the tree:**

- DFS

**Determining whether a path exists between two nodes:**

- DFS

**Finding the shortest path:**

- BFS