import heapq


def best_first_search(graph, start, goal, heuristic):
    frontier = [(heuristic(start, goal), start)]
    visited = set()

    while frontier:
        _, current_node = heapq.heappop(frontier)

        if current_node == goal:
            return current_node

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                priority = heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))

    return None


# Example usage:
graph = {"A": ["B", "C"], "B": ["D", "E"], "C": ["F"], "D": [], "E": ["F"], "F": []}


# Example heuristic function (Euclidean distance)
def heuristic(node, goal):
    # Assuming node and goal are strings representing nodes in the graph
    return 0  # Replace this with your actual heuristic calculation


start_node = "A"
goal_node = "F"
print(best_first_search(graph, start_node, goal_node, heuristic))
