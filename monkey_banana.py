class MonkeyBananaProblem:
    def __init__(self):
        # Initial state
        self.monkey_position = 'floor'  # Options: 'floor', 'box', 'bananas'
        self.box_position = 'floor'      # Options: 'floor', 'under bananas'
        self.banana_position = 'high'     # Options: 'high', 'low'
        self.has_banana = False            # Whether the monkey has the bananas

    def move_box(self):
        if self.box_position == 'floor':
            print("Monkey moves the box under the bananas.")
            self.box_position = 'under bananas'
        else:
            print("Box is already under the bananas.")

    def climb_box(self):
        if self.box_position == 'under bananas' and self.monkey_position == 'floor':
            print("Monkey climbs onto the box.")
            self.monkey_position = 'box'
        elif self.box_position == 'under bananas' and self.monkey_position == 'box':
            print("Monkey is already on the box.")
        else:
            print("Monkey can't climb the box because it is not under the bananas.")

    def take_bananas(self):
        if self.monkey_position == 'box' and self.banana_position == 'high':
            print("Monkey takes the bananas.")
            self.has_banana = True
            self.banana_position = 'low'  # Assume the bananas are now on the floor after taking them
        else:
            print("Monkey can't take the bananas. Either not on the box or bananas are not reachable.")

    def solve(self):
        print("Starting the Monkey and Banana Problem...")
        
        # Step 1: Move the box under the bananas
        self.move_box()
        
        # Step 2: Climb on the box
        self.climb_box()
        
        # Step 3: Take the bananas
        self.take_bananas()
        
        if self.has_banana:
            print("Monkey has successfully retrieved the bananas!")
        else:
            print("Monkey failed to retrieve the bananas.")

# Example usage
if __name__ == "__main__":
    problem = MonkeyBananaProblem()
    problem.solve()