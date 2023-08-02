import heapq


class PuzzleNode:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other): #The __lt__() method is used to compare the priority of two nodes based on their heuristic_cost.
        return self.f < other.f
"""
    def __eq__(self, other):
        return str(self.state) == str(other.state)
"""

def find_blank_square(state):
    for i, row in enumerate(state):
        for j, val in enumerate(row):
            if val == 0:
                return i, j

def actions(state):
    moves = []
    row, col = find_blank_square(state)
    if row > 0:
        moves.append(('up', (row - 1, col)))
    if row < 2:
        moves.append(('down', (row + 1, col)))
    if col > 0:
        moves.append(('left', (row, col - 1)))
    if col < 2:
        moves.append(('right', (row, col + 1)))
    return moves

def apply_action(state, action): 
    row, col = find_blank_square(state)
    dr, dc = action[1][0] - row, action[1][1] - col
    new_state = [row[:] for row in state]
    new_state[row][col], new_state[row + dr][col + dc] = new_state[row + dr][col + dc], new_state[row][col]
    
    return new_state
    
def heuristic(state):
    count = 0   
    for i, row in enumerate(state):
        for j, val in enumerate(row):
            if val != 0:
                goal_row = (val - 1) // 3
                goal_col = (val - 1) % 3
                # These lines calculate the goal position (i.e., where the number should be in the goal state) 
                count += abs(i - goal_row) + abs(j - goal_col)
                
                # P1 = (1,1)
                # P2 = (3,2)
                # Manhaten Distance = |(3-1) + (3-2)| = 3
    return count

def a_star_search(initial_state):
    initial_node = PuzzleNode(state=initial_state, g=0, h=heuristic(initial_state))
    heap = [initial_node]
    visited = set()

    print("Initial board:")
    print_board(initial_state) 

    current_level = -1 # Initialize current_level to -1

    while heap:
        current_node = heapq.heappop(heap)
        
        # Check if we've moved to a new level
        if current_node.g > current_level:
            current_level = current_node.g
            print("-----------------------------------------------------------------------------------")
            print("Level:", current_level)
        
        if current_node.state == goal_state:
            print("Goal board found!")
            print(" Cost = {} | H={} |G={}".format( current_node.f, current_node.h , current_node.g))
            print_board(current_node.state)
            return current_node
        visited.add(str(current_node.state))
        for action in actions(current_node.state):
            new_state = apply_action(current_node.state, action)
            if str(new_state) not in visited:
                g = current_node.g + 1
                h = heuristic(new_state)
                new_node = PuzzleNode(state=new_state, parent=current_node, action=action, g=g, h=h)
                heapq.heappush(heap, new_node)
                print("Board after {} move: Cost = {} | H={} |G={}".format(action[0], new_node.f, new_node.h , new_node.g))
                print_board(new_state, action=action[0], parent_state=current_node.state)
                
    return None


def print_board(state, action=None, parent_state=None):
    if action:
        print("Action: ", action)
    if parent_state:
        print("Parent state: ")
        for row in parent_state:
            print(row)
        print()
    print("Current state: ")
    for row in state:
        print(row)
    print()

# Example usage:
initial_state = [[2, 8, 3],
                 [1, 6, 4],
                 [7, 0, 5]]

goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

result = a_star_search(initial_state)

if result:
    moves = []
    node = result
    while node.parent is not None:
        moves.append(node.action[0])
        node = node.parent
    moves
    print("Solution found in {} ".format(len(moves)))
    print("Moves: {}".format(moves))
else:
    print("No solution found.")