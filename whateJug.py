def water_jug_BFS(capacities, target):
    from collections import deque
    
    # Initialize visited set and queue for BFS
    visited = set()
    queue = deque()
    
    # Initial state (all jugs empty)
    initial_state = tuple([0] * len(capacities))
    queue.append((initial_state, []))
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        
        # Check if target is reached in any jug
        if target in current_state:
            return path + [current_state]
            
        # Generate all possible next states
        for i in range(len(capacities)):
            # Fill jug i
            new_state = list(current_state)
            new_state[i] = capacities[i]
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))
            
            # Empty jug i
            new_state = list(current_state)
            new_state[i] = 0
            new_state = tuple(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))
            
            # Pour from jug i to other jugs
            for j in range(len(capacities)):
                if i != j:
                    new_state = list(current_state)
                    # Calculate how much water can be poured
                    amount = min(current_state[i], capacities[j] - current_state[j])
                    new_state[i] -= amount
                    new_state[j] += amount
                    new_state = tuple(new_state)
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, path + [current_state]))
    
    return None  # If no solution is found

def print_solution(solution):
    if solution is None:
        print("No solution exists!")
        return
        
    print("\nSolution found! Steps:")
    for i, state in enumerate(solution):
        print(f"Step {i}: {state}")
    print(f"\nTotal steps required: {len(solution) - 1}")

def main():
    # Get user input
    n = int(input("Enter the number of jugs: "))
    capacities = []
    print("\nEnter the capacity of each jug:")
    for i in range(n):
        capacity = int(input(f"Jug {i+1}: "))
        capacities.append(capacity)
    
    target = int(input("\nEnter the desired amount of water to measure: "))
    
    # Solve the problem
    print("\nSolving...")
    solution = water_jug_BFS(tuple(capacities), target)
    print_solution(solution)

if __name__ == "__main__":
    main()