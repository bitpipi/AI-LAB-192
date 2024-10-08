def manhattan(puzzle, goal):
    dist = 0
    for i in range(9):
        if puzzle[i] != 0:
            goal_idx = goal.index(puzzle[i])
            dist += abs(i // 3 - goal_idx // 3) + abs(i % 3 - goal_idx % 3)
    return dist

def dfs_manhattan(puzzle, goal, visited, path):
    if puzzle == goal:
        return path
    visited.add(tuple(puzzle))
    idx = puzzle.index(0)
    moves = [(1, 3), (-1, 3), (3, 1), (-3, 1)]
    next_states = []
    for move, cond in moves:
        new_idx = idx + move
        if 0 <= new_idx < 9 and (new_idx // 3 == idx // 3 or new_idx % 3 == idx % 3):
            new_puzzle = puzzle[:]
            new_puzzle[idx], new_puzzle[new_idx] = new_puzzle[new_idx], new_puzzle[idx]
            if tuple(new_puzzle) not in visited:
                next_states.append((new_puzzle, manhattan(new_puzzle, goal)))
    next_states.sort(key=lambda x: x[1])
    for state, _ in next_states:
        res = dfs_manhattan(state, goal, visited, path + [state])
        if res:
            return res
    return None

def prettify(res):
    i=0
    for j in range(3):
        for k in range(3):
            print(res[i],end=" ")
            i+=1
        print("\n")
start = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goal = [0,1, 2, 3, 4, 5, 6, 7, 8]
result = dfs_manhattan(start, goal, set(), [start])

for i in result:
    prettify(i)
    print("--------")
