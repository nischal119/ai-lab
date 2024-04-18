import heapq


def astar_search(graph, start, goal, heuristic):
    open_list = [(0, start)]  # Priority queue (f(n), node)
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    parent = {}

    while open_list:
        f_score, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(parent, current_node)

        for neighbor in graph[current_node]:
            tentative_g_score = g_score[current_node] + 1  # Assuming unweighted edges
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))
                parent[neighbor] = current_node

    return None


def reconstruct_path(parent, goal):
    path = [goal]
    while goal in parent:
        goal = parent[goal]
        path.append(goal)
    return list(reversed(path))


# Example usage:
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": [],
}


# Example heuristic function (Euclidean distance)
def heuristic(node, goal):
    # Assuming node and goal are strings representing nodes in the graph
    return 0  # Replace this with your actual heuristic calculation


start_node = "A"
goal_node = "F"
print(astar_search(graph, start_node, goal_node, heuristic))
