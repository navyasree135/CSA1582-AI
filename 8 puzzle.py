import heapq

class PuzzleState:
    def __init__(self, board, g=0, parent=None):
        self.board = board
        self.g = g  # Cost to reach this state
        self.parent = parent  # Parent state
        self.f = self.g + self.h()  # Total cost (g + heuristic)

    def __lt__(self, other):
        return self.f < other.f

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(self.board))

    def h(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        return sum(abs((self.board.index(i) % 3) - (goal.index(i) % 3)) +
                   abs((self.board.index(i) // 3) - (goal.index(i) // 3))
                   for i in range(1, 9))

    def get_neighbors(self):
        neighbors = []
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        zero_index = self.board.index(0)
        zero_x, zero_y = zero_index % 3, zero_index // 3

        for dx, dy in moves:
            new_x, new_y = zero_x + dx, zero_y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_index = new_y * 3 + new_x
                new_board = self.board[:]
                new_board[zero_index], new_board[new_index] = new_board[new_index], new_board[zero_index]
                neighbors.append(PuzzleState(new_board, self.g + 1, self))
        return neighbors

def solve_8_puzzle(initial_state):
    open_list = []
    closed_list = set()
    initial_state = PuzzleState(initial_state)
    heapq.heappush(open_list, initial_state)

    while open_list:
        current_state = heapq.heappop(open_list)
        if current_state.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
            path = []
            total_cost = current_state.g  # Cost to reach the goal state
            while current_state:
                path.append(current_state.board)
                current_state = current_state.parent
            return path[::-1], total_cost  # Return solution path and total cost
        closed_list.add(current_state)
        for neighbor in current_state.get_neighbors():
            if neighbor in closed_list:
                continue
            if neighbor not in open_list:
                heapq.heappush(open_list, neighbor)
            else:
                index = open_list.index(neighbor)
                if open_list[index].g > neighbor.g:
                    open_list[index].g = neighbor.g
                    open_list[index].parent = current_state
                    heapq.heapify(open_list)
    return None, None

# Take user input for the initial state
try:
    initial_state = list(map(int, input("Enter the 8-puzzle board as 9 numbers separated by spaces (0 for the empty tile): ").split()))
    if len(initial_state) != 9:
        print("Invalid input. Please enter exactly 9 numbers.")
    else:
        solution, total_cost = solve_8_puzzle(initial_state)
        if solution:
            print("Solution Path:")
            for state in solution:
                print(state)
            print(f"Total Cost (Number of Moves): {total_cost}")
        else:
            print("No solution found.")
except ValueError:
    print("Invalid input. Please ensure all inputs are integers.")
