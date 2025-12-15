visited = set()

def safe(mL, cL, mR, cR):
    if mL < 0 or cL < 0 or mR < 0 or cR < 0:
        return False
    if (mL > 0 and mL < cL): return False
    if (mR > 0 and mR < cR): return False
    return True

def solve(mL, cL, mR, cR, boat):
    if (mL, cL, mR, cR, boat) in visited:
        return False
    visited.add((mL, cL, mR, cR, boat))

    print(mL, cL, mR, cR, boat)  # print state

    if mL == 0 and cL == 0:
        return True

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

    for m, c in moves:
        if boat == 'L':
            new = (mL-m, cL-c, mR+m, cR+c, 'R')
        else:
            new = (mL+m, cL+c, mR-m, cR-c, 'L')

        if safe(new[0], new[1], new[2], new[3]):
            if solve(*new):
                return True

    return False

solve(3, 3, 0, 0, 'L')
