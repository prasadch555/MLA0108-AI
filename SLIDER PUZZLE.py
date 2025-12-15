
puzzle = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

def print_puzzle(p):
    for row in p:
        print(row)
    print()

print("Initial Puzzle:")
print_puzzle(puzzle)

puzzle[1][1], puzzle[2][1] = puzzle[2][1], puzzle[1][1]

print("After First Move:")
print_puzzle(puzzle)

puzzle[2][1], puzzle[2][2] = puzzle[2][2], puzzle[2][1]

print("After Second Move:")
print_puzzle(puzzle)
