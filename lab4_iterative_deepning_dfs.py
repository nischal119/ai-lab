def iddfs(graph, start, goal):
    depth_limit = 0
    while True:
        result = dfs_limit(graph, start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1


def dfs_limit(graph, node, goal, depth_limit, depth=0, visited=None):
    if visited is None:
        visited = set()

    if node == goal:
        return node

    if depth >= depth_limit:
        return None

    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            result = dfs_limit(graph, neighbor, goal, depth_limit, depth + 1, visited)
            if result is not None:
                return result

    return None


# Example usage:
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}
start_node = "A"
goal_node = "F"
print(iddfs(graph, start_node, goal_node))
