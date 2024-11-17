import heapq
from typing import List, Tuple

# Define the goal state
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

class PuzzleNode:
    def __init__(self, state: Tuple[int, ...], parent, g: int, h: int):
        self.state = state
        self.parent = parent
        self.g = g  # Cost to reach this node
        self.h = h  # Heuristic estimate to goal

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def get_blank_position(state: Tuple[int, ...]) -> int:
    return state.index(0)

def get_manhattan_distance(state: Tuple[int, ...]) -> int:
    distance = 0
    for i in range(9):
        if state[i] != 0:
            correct_row = (state[i] - 1) // 3
            correct_col = (state[i] - 1) % 3
            current_row = i // 3
            current_col = i % 3
            distance += abs(correct_row - current_row) + abs(correct_col - current_col)
    return distance

def get_neighbors(state: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    neighbors = []
    blank = get_blank_position(state)
    for move in [-3, -1, 1, 3]:  # Up, Left, Right, Down
        new_pos = blank + move
        if 0 <= new_pos < 9 and abs(blank % 3 - new_pos % 3) <= 1:
            new_state = list(state)
            new_state[blank], new_state[new_pos] = new_state[new_pos], new_state[blank]
            neighbors.append(tuple(new_state))
    return neighbors

def solve_puzzle(initial_state: Tuple[int, ...]) -> List[Tuple[int, ...]]:
    start_node = PuzzleNode(initial_state, None, 0, get_manhattan_distance(initial_state))
    open_list = [start_node]
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == GOAL_STATE:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node.state)

        for neighbor_state in get_neighbors(current_node.state):
            if neighbor_state in closed_set:
                continue

            g = current_node.g + 1
            h = get_manhattan_distance(neighbor_state)
            neighbor_node = PuzzleNode(neighbor_state, current_node, g, h)

            if neighbor_node not in open_list:
                heapq.heappush(open_list, neighbor_node)
            else:
                idx = open_list.index(neighbor_node)
                if open_list[idx].g > g:
                    open_list[idx] = neighbor_node
                    heapq.heapify(open_list)

    return None  # No solution found

def print_puzzle(state: Tuple[int, ...]):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def get_user_input():
    print("Enter the initial state of the puzzle (space-separated numbers):")
    print("Example: 1 2 3 4 5 6 7 8 0")
    user_input = input().split()
    if len(user_input) != 9:
        print("Invalid input. Please enter 9 numbers.")
        return get_user_input()
    try:
        initial_state = tuple(int(x) for x in user_input)
        if 0 not in initial_state or len(set(initial_state)) != 9:
            print("Invalid input. Please enter a valid puzzle state.")
            return get_user_input()
        return initial_state
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return get_user_input()

def main():
    initial_state = get_user_input()
    solution = solve_puzzle(initial_state)

    if solution:
        print("Solution found!")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            print_puzzle(state)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()