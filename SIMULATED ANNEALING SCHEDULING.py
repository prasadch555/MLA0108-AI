import random, math

tasks = ["T1","T2","T3","T4","T5","T6"]
slots = [0,1,2]

# Random initial schedule
def make_schedule():
    return [random.choice(slots) for _ in tasks]

# Cost = how many tasks crowd in each slot
def cost(s):
    c = [0,0,0]
    for x in s: c[x] += 1
    return sum(v*v for v in c)

# Neighbor = change slot of one task
def neighbor(s):
    n = s[:]
    i = random.randrange(len(tasks))
    n[i] = random.choice(slots)
    return n

def sa():
    T = 100
    curr = make_schedule()
    best = curr[:]
    while T > 0.1:
        nxt = neighbor(curr)
        d = cost(nxt) - cost(curr)
        if d < 0 or random.random() < math.exp(-d/T):
            curr = nxt
        if cost(curr) < cost(best):
            best = curr[:]
        T *= 0.95
    return best, cost(best)

best, c = sa()
print("Best Schedule:", best)
print("Cost:", c)
