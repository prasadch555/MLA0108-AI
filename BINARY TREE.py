# Simple Minimax for a depth-2 perfect binary tree

def minimax(values):
    # values = [A, B, C, D] (leaf scores)

    # Level 1: MIN nodes
    left_min  = min(values[0], values[1])
    right_min = min(values[2], values[3])

    # Level 0: MAX root decision
    best_move = max(left_min, right_min)

    if best_move == left_min:
        return "Go LEFT subtree", best_move
    else:
        return "Go RIGHT subtree", best_move

# ---- Input ----
vals = list(map(int, input("Enter 4 leaf values (A B C D): ").split()))

move, score = minimax(vals)

print("Best Move for MAX player:", move)
print("Guaranteed Score:", score)
