facts = ["vertebrate(duck)", "flying(duck)", "mammal(cat)"]

rules = {
    "vertebrate(X)": ["mammal(X)"],
    "animal(X)": ["vertebrate(X)"],
    "bird(X)": ["vertebrate(X)", "flying(X)"]
}

def bc(goal):
    if goal in facts:
        return True
    gname, garg = goal[:-1].split("(")
    for head, body in rules.items():
        hname, harg = head[:-1].split("(")
        if gname == hname:
            if all(bc(b.replace(harg, garg)) for b in body):
                return True
    return False

# Test
for q in ["animal(duck)", "bird(duck)", "animal(cat)", "bird(cat)"]:
    print(q, ":", bc(q))
