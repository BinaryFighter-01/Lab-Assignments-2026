import random

# Distance matrix (example 4 cities)
dist = [
    [0, 2, 9, 10],
    [2, 0, 6, 4],
    [9, 6, 0, 8],
    [10, 4, 8, 0]
]

n = len(dist)
pher = [[1]*n for _ in range(n)]  # pheromone

# Build path for one ant
def path():
    p = [0]
    unvisited = list(range(1, n))
    while unvisited:
        probs = []
        for j in unvisited:
            probs.append(pher[p[-1]][j] * (1/dist[p[-1]][j]))
        s = sum(probs)
        r = random.random()
        cum = 0
        for i, j in enumerate(unvisited):
            cum += probs[i]/s
            if r <= cum:
                p.append(j)
                unvisited.remove(j)
                break
    return p

# Path length
def length(p):
    return sum(dist[p[i]][p[i+1]] for i in range(len(p)-1)) + dist[p[-1]][p[0]]

# ACO loop
for _ in range(10):
    paths = [path() for _ in range(5)]
    for i in range(n):
        for j in range(n):
            pher[i][j] *= 0.5  # evaporation
    for p in paths:
        l = length(p)
        for i in range(len(p)-1):
            pher[p[i]][p[i+1]] += 1/l  # deposit

# Best path
best = min(paths, key=length)
print("Best Path:", best)
print("Distance:", length(best))