import random

# Target we want to match (optimization goal)
target = [1, 0, 1, 1]

# Create random antibody (solution)
def create():
    return [random.randint(0,1) for _ in target]

# Fitness = how many bits match target
def fitness(x):
    return sum([1 for i in range(len(x)) if x[i] == target[i]])

# Mutation (flip bit with small probability)
def mutate(x):
    return [bit if random.random() > 0.3 else 1-bit for bit in x]

# Initial population
pop = [create() for _ in range(6)]

# Algorithm loop
for _ in range(5):
    pop = sorted(pop, key=fitness, reverse=True)[:2] + \
          [mutate(x) for x in pop]

# Best solution
best = max(pop, key=fitness)
print("Best:", best, "Fitness:", fitness(best))