from pulp import LpVariable, LpProblem, lpSum, value

def crossword_solver(words, puzzle):
    problem = LpProblem("Crossword_Solver", sense=1)

    # Create variables
    locations = [(i, j, k) for i in range(len(words)) for j in range(len(words[0])) for k in range(10)]
    x = LpVariable.dicts("x", locations, cat='Binary')

    # Objective function (minimize the total number of words placed)
    problem += lpSum([x[i, j, k] for i in range(len(words)) for j in range(len(words[0])) for k in range(10)])

    # Constraints for horizontal words
    for i in range(len(words)):
        for j in range(len(words[0])):
            problem += lpSum([x[i, j, k] for k in range(10)]) == 1

    # Constraints for vertical words
    for j in range(len(words[0])):
        for i in range(len(words)):
            problem += lpSum([x[i, j, k] for k in range(10)]) == 1

    # Constraints for word placement
    for i in range(len(words)):
        for j in range(len(words[0])):
            for k in range(10 - len(words[i]) + 1):
                problem += lpSum([x[i, j, k + l] for l in range(len(words[i]))]) <= len(words[i])
    problem.solve()
    solution = {word: [] for word in words}
    for i in range(len(words)):
        for j in range(len(words[0])):
            for k in range(10):
                if value(x[i, j, k]) == 1:
                    solution[words[i]].append((j, k))

    return solution
puzzle = [
    [None, None, None, None, None],
    [None, None, 'h', None, None],
    [None, None, None, None, None],
    [None, None, 'v', None, None],
    [None, None, None, None, None],
]

words = ['hello', 'halo', 'hive', 'velvet', 'even']

solution = crossword_solver(words, puzzle)

if solution:
    for word in words:
        print(f"{word}: {solution[word]}")
else:
    print("No solution found.")
