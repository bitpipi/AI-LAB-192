import heapq

def manhattan(puzzle, goal):
    dist = 0
    for i in range(9):
        if puzzle[i] != 0:
            goal_idx = goal.index(puzzle[i])
            dist += abs(i // 3 - goal_idx // 3) + abs(i % 3 - goal_idx % 3)
    return dist

def a_star_manhattan(puzzle, goal):
    # Priority queue for A* search, stores tuples of (cost, puzzle_state, path)
    pq = [(manhattan(puzzle, goal), puzzle, [puzzle])]
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)
        
        if current == goal:
            return path

        visited.add(tuple(current))
        idx = current.index(0)
        # Define possible moves for the blank space
        moves = [(1, 3), (-1, 3), (3, 1), (-3, 1)]
        
        for move, cond in moves:
            new_idx = idx + move
            if 0 <= new_idx < 9 and (new_idx // 3 == idx // 3 or new_idx % 3 == idx % 3):
                new_puzzle = current[:]
                new_puzzle[idx], new_puzzle[new_idx] = new_puzzle[new_idx], new_puzzle[idx]
                
                if tuple(new_puzzle) not in visited:
                    heapq.heappush(pq, (cost + manhattan(new_puzzle, goal), new_puzzle, path + [new_puzzle]))

    return None

def prettify_step(step, index):
    print(f"Step {index}:")
    for i in range(0, 9, 3):
        print(f"{step[i]} {step[i+1]} {step[i+2]}")
    print("-" * 8)

start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Run A* search
result = a_star_manhattan(start, goal)

# Print the solution steps, but limit to every 2nd step for brevity
if result:
    for index, step in enumerate(result):
        if index % 2 == 0:  # Print only every 2nd step
            prettify_step(step, index)
    print(f"Total moves: {len(result)}")
else:
    print("No solution found.")
