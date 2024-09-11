import random

# Define the grid environment for the vacuum cleaner
class VacuumCleaner:
    def __init__(self):
        # A 2x2 grid where 0 represents clean and 1 represents dirty
        self.grid = [[random.choice([0, 1]), random.choice([0, 1])],
                     [random.choice([0, 1]), random.choice([0, 1])]]
        # Vacuum cleaner's initial position (0,0) i.e. top-left
        self.position = [0, 0]

    # Method to display the grid and cleaner's position
    def display_grid(self):
        print("Grid Status:")
        for i in range(2):
            for j in range(2):
                if [i, j] == self.position:
                    print(f"[C]", end=" ")  # C for cleaner
                else:
                    print(f"[{self.grid[i][j]}]", end=" ")
            print()
        print()

    # Method to clean the current position if it's dirty
    def clean(self):
        x, y = self.position
        if self.grid[x][y] == 1:
            print(f"Cleaning position {self.position}")
            self.grid[x][y] = 0
        else:
            print(f"Position {self.position} is already clean")

    # Method to move the vacuum cleaner to a new position
    def move(self, direction):
        if direction == 'left' and self.position[1] > 0:
            self.position[1] -= 1
        elif direction == 'right' and self.position[1] < 1:
            self.position[1] += 1
        elif direction == 'up' and self.position[0] > 0:
            self.position[0] -= 1
        elif direction == 'down' and self.position[0] < 1:
            self.position[0] += 1
        print(f"Moved {direction} to {self.position}")

    # Check if all the squares are clean
    def all_clean(self):
        for row in self.grid:
            if 1 in row:
                return False
        return True

# Main function simulating the vacuum cleaner's actions
def vacuum_cleaner_simulation():
    vacuum = VacuumCleaner()

    while not vacuum.all_clean():
        vacuum.display_grid()
        vacuum.clean()

        # Instead of moving randomly, the vacuum will move systematically
        x, y = vacuum.position

        # Move to the next square in a systematic order (right -> down -> left -> up)
        if x == 0 and y == 0:
            vacuum.move('right')
        elif x == 0 and y == 1:
            vacuum.move('down')
        elif x == 1 and y == 1:
            vacuum.move('left')
        elif x == 1 and y == 0:
            vacuum.move('up')

    print("All squares are clean!")
    vacuum.display_grid()

if __name__ == "__main__":
    vacuum_cleaner_simulation()
