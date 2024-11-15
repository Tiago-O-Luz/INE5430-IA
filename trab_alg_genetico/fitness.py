# List of items as pairs of (weight, value)
# For this example:
# items = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
# maximum_capacity = 10

# Example 2: New set of items and capacity
items = [(3, 5), (5, 8), (6, 9), (7, 13), (4, 7), (2, 4)]
maximum_capacity = 15

# Calculate the maximum possible value (used in fitness function to normalize)
max_value = sum([v[1] for v in items])

# Define the fitness function to evaluate each solution
def fitness_func(ga_instance, solution, solution_idx):
    # Calculate the total weight and total value of the current solution
    weight = sum([v * items[i][0] for i, v in enumerate(solution)])
    value = sum([v * items[i][1] for i, v in enumerate(solution)])
    
    # If the weight exceeds the maximum capacity, return fitness as 0 (invalid solution)
    if weight > maximum_capacity:
        return 0
    
    # Calculate fitness as the inverse of the difference between max value and current value
    # This encourages solutions with higher values to have a higher fitness score
    fitness = 1 / abs(max_value - value)

    return fitness
