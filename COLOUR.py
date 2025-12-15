import random

def epsilon_greedy(epsilon, rounds=50):
    rewards = [2, 5, 3]      # deterministic rewards
    Q = [0, 0, 0]            # estimated values
    counts = [0, 0, 0]       # number of pulls
    total_reward = 0

    for _ in range(rounds):
        # exploration
        if random.random() < epsilon:
            action = random.randint(0, 2)
        else:
            action = Q.index(max(Q))   # exploitation

        # receive reward
        r = rewards[action]
        total_reward += r

        # update estimates
        counts[action] += 1
        Q[action] += (r - Q[action]) / counts[action]

    return total_reward

# Compare epsilon = 0.1 and 0.3
cum_01 = epsilon_greedy(0.1)
cum_03 = epsilon_greedy(0.3)

print("Cumulative Reward (epsilon = 0.1):", cum_01)
print("Cumulative Reward (epsilon = 0.3):", cum_03)
