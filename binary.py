from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Build the CAJES Binary Tree
# Level 0
root = Node('C')

# Level 1
root.left = Node('A')
root.right = Node('J')

# Level 2
root.left.left = Node('E')
root.left.right = Node('S')


# 1. Breadth-First Search (BFS)
def bfs(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


# 2. Depth-First Search (DFS)
def dfs(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.value)
        dfs(node.left, result)
        dfs(node.right, result)
    return result


if __name__ == "__main__":
    print("=== CAJES Binary Tree Traversals ===")
    print("BFS:", " -> ".join(bfs(root)))
    print("DFS:", " -> ".join(dfs(root)))