def tsp(graph, start):
    # Get all vertices except the starting point
    vertices = list(graph.keys())
    vertices.remove(start)
    
    min_path = float('inf')
    min_path_route = []
    
    def find_paths(curr_vertex, unvisited, path, cost):
        nonlocal min_path, min_path_route
        
        # Base case: all cities have been visited
        if not unvisited:
            # Add cost to return to starting city
            total_cost = cost + graph[curr_vertex][start]
            if total_cost < min_path:
                min_path = total_cost
                min_path_route = path + [start]
            return
            
        # Try visiting each unvisited city
        for next_vertex in unvisited:
            # Calculate new cost
            new_cost = cost + graph[curr_vertex][next_vertex]
            # Skip if cost already exceeds minimum found
            if new_cost < min_path:
                # Create new unvisited set excluding next_vertex
                new_unvisited = unvisited.copy()
                new_unvisited.remove(next_vertex)
                # Recursive call
                find_paths(next_vertex, new_unvisited, path + [next_vertex], new_cost)
    
    # Start the recursive search
    find_paths(start, set(vertices), [start], 0)
    
    return min_path, min_path_route

# Example usage:
def main():
    # Get number of cities
    n = int(input("Enter number of cities: "))
    
    # Create empty graph
    graph = {}
    
    # Get city names
    print("\nEnter city names:")
    cities = []
    for i in range(n):
        city = input(f"City {i+1}: ")
        cities.append(city)
        graph[city] = {}
    
    # Get distances between cities
    print("\nEnter distances between cities:")
    for i in range(n):
        for j in range(i+1, n):
            dist = int(input(f"Distance between {cities[i]} and {cities[j]}: "))
            graph[cities[i]][cities[j]] = dist
            graph[cities[j]][cities[i]] = dist
    
    # Get starting city
    start = input("\nEnter starting city: ")
    
    # Find shortest path
    distance, path = tsp(graph, start)
    
    # Print results
    print("\nShortest Route:")
    print(" -> ".join(path))
    print(f"Total Distance: {distance}")

# Alternative example with hardcoded values:
def example():
    # Example graph using dictionary
    graph = {
        'A': {'B': 10, 'C': 15, 'D': 20},
        'B': {'A': 10, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'D': 30},
        'D': {'A': 20, 'B': 25, 'C': 30}
    }
    
    # Find shortest path starting from city 'A'
    distance, path = tsp(graph, 'A')
    
    # Print results
    print("\nShortest Route:")
    print(" -> ".join(path))
    print(f"Total Distance: {distance}")

if __name__ == "__main__":
    # Choose whether to use manual input or example
    choice = input("Enter '1' for manual input or '2' for example: ")
    if choice == '1':
        main()
    else:
        example()