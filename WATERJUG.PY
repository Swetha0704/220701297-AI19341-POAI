WATERJUG
def dfs_solution(jug1, jug2, target): 
    visited = set() 
    stack = [(0, 0)] 
    while stack: 
        state = stack.pop() 
        if state in visited: 
            continue 
        visited.add(state) 
        x, y = state 
        if x == target or y == target: 
            return f"Solution: {state}" 
        next_states = [ 
            (jug1, y), 
            (x, jug2), 
            (0, y), 
            (x, 0), 
            (min(x + y, jug1), max(0, x + y - jug1)), 
            (max(0, x + y - jug2), min(x + y, jug2)) 
        ] 
        for next_state in next_states: 
            if next_state not in visited: 
                stack.append(next_state) 
    return "No solution." 
jug1 = int(input("Enter capacity of Jug 1: ")) 
jug2 = int(input("Enter capacity of Jug 2: ")) 
target = int(input("Enter target amount: ")) 
print(dfs_solution(jug1, jug2, target)) 
