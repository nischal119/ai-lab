import random


def hill_climbing(problem, max_iterations):
    current_solution = problem.initial_solution()
    for _ in range(max_iterations):
        neighbors = problem.generate_neighbors(current_solution)
        best_neighbor = max(neighbors, key=lambda neighbor: problem.evaluate(neighbor))
        if problem.evaluate(best_neighbor) <= problem.evaluate(current_solution):
            return current_solution
        current_solution = best_neighbor
    return current_solution


# Example usage:
class OptimizationProblem:
    def initial_solution(self):
        return [
            random.uniform(-10, 10) for _ in range(5)
        ]  # Example: 5-dimensional solution space

    def generate_neighbors(self, solution):
        neighbors = []
        for _ in range(5):  # Example: Generate 5 random neighboring solutions
            neighbor = list(solution)
            index = random.randint(0, len(solution) - 1)
            neighbor[index] += random.uniform(
                -1, 1
            )  # Example: Make a small modification
            neighbors.append(neighbor)
        return neighbors

    def evaluate(self, solution):
        return sum(x**2 for x in solution)  # Example: Minimize the sum of squares


problem = OptimizationProblem()
best_solution = hill_climbing(problem, 1000)
print("Best solution:", best_solution)
print("Objective value:", problem.evaluate(best_solution))
