from queue import PriorityQueue

class PuzzleState:
    def __init__(self, board, zero_pos, moves=0, previous=None):
        self.board = board
        self.zero_pos = zero_pos
        self.moves = moves
        self.previous = previous

    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

    def heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        goal_positions = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                          4: (1, 0), 5: (1, 1), 6: (1, 2),
                          7: (2, 0), 8: (2, 1), 0: (2, 2)}
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                goal_x, goal_y = goal_positions[value]
                distance += abs(goal_x - i) + abs(goal_y - j)
        return distance

    def get_neighbors(self):
        # Possible moves (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbors = []
        x, y = self.zero_pos

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                # Swap the zero with the adjacent tile
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, (new_x, new_y), self.moves + 1, self))

        return neighbors

def a_star(start, goal):
    start_zero_pos = next((i, j) for i in range(3) for j in range(3) if start[i][j] == 0)
    goal_flat = [value for row in goal for value in row]

    open_set = PriorityQueue()
    open_set.put(PuzzleState(start, start_zero_pos))
    visited = set()

    while not open_set.empty():
        current_state = open_set.get()
        current_board_tuple = tuple(tuple(row) for row in current_state.board)
        visited.add(current_board_tuple)

        if current_state.board == goal:
            print("Solution found in", current_state.moves, "moves.")
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.previous
            for step in reversed(path):
                for row in step:
                    print(row)
                print()
            return

        for neighbor in current_state.get_neighbors():
            neighbor_board_tuple = tuple(tuple(row) for row in neighbor.board)
            if neighbor_board_tuple not in visited:
                open_set.put(neighbor)

    print("No solution found.")


def get_input_state(prompt):
    while True:
        state_input = input(prompt)
        try:
            state = list(map(int, state_input.split()))
            if len(state) == 9 and all(x in range(9) for x in state):
                return [state[i:i+3] for i in range(0, 9, 3)]
            else:
                print("Invalid input. Please enter 9 numbers (0-8).")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

def main():
    print("Enter the start state (9 numbers, use 0 for the blank space):")
    start_state = get_input_state("Start state: ")

    print("Enter the goal state (9 numbers, use 0 for the blank space):")
    goal_state = get_input_state("Goal state: ")

    a_star(start_state, goal_state)

if __name__ == "__main__":
    main()

