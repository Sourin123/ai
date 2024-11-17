class AlphaBetaPruning:
    def __init__(self):
        self.nodes_evaluated = 0  # To count the number of nodes evaluated

    def minimax(self, node, depth, alpha, beta, maximizing_player):
        # Base case: If depth is 0 or node is a terminal node, return the heuristic value
        if depth == 0 or self.is_terminal(node):
            self.nodes_evaluated += 1
            return self.evaluate(node)

        if maximizing_player:
            max_eval = float('-inf')
            for child in self.get_children(node):
                eval = self.minimax(child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)

                # Alpha-beta pruning
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for child in self.get_children(node):
                eval = self.minimax(child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)

                # Alpha-beta pruning
                if beta <= alpha:
                    break
            return min_eval

    def is_terminal(self, node):
        # Check if the node is a terminal node (game over)
        # This function should be defined based on the game logic
        return len(self.get_children(node)) == 0

    def evaluate(self, node):
        # Evaluate the node (heuristic function)
        # This function should be defined based on the game logic
        return node  # Replace with actual evaluation logic

    def get_children(self, node):
        # Generate the children of the current node
        # This function should be defined based on the game logic
        return [node - 1, node - 2, node - 3]  # Example children

    def run(self, initial_node, depth):
        alpha = float('-inf')
        beta = float('inf')
        best_value = self.minimax(initial_node, depth, alpha, beta, True)
        print(f"Best value: {best_value}")
        print(f"Nodes evaluated: {self.nodes_evaluated}")


# Example usage:
if __name__ == "__main__":
    initial_node = 10 # Starting point
    depth = 3        # Depth of the search tree
    alpha_beta = AlphaBetaPruning()
    alpha_beta.run(initial_node, depth)