def solve(board=[], row=0):
    if row == 8:
        for r in range(8):
            print(" ".join("Q" if board[r]==c else "." for c in range(8)))
        return True
    for col in range(8):
        if all(board[i] != col and abs(board[i]-col) != row-i for i in range(row)):
            board.append(col)
            if solve(board, row+1): return True
            board.pop()
    return False

solve()
