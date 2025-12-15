def ab(a, d, m, al, be):
    if d == 0 or type(a) == int:
        return a

    if m:  # MAX
        v = -999
        for x in a:
            v = max(v, ab(x, d-1, 0, al, be))
            al = max(al, v)
            if be <= al:
                break
        return v

    else:  # MIN
        v = 999
        for x in a:
            v = min(v, ab(x, d-1, 1, al, be))
            be = min(be, v)
            if be <= al:
                break
        return v


t = eval(input())
print(ab(t, 3, 1, -999, 999))
