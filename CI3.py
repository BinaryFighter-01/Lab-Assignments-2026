import random

t = [1,0,1,1]

def f(x): return sum(x[i]==t[i] for i in range(len(t)))
def m(x): return [b if random.random()>0.3 else 1-b for b in x]

p = [[random.randint(0,1) for _ in t] for _ in range(6)]

for _ in range(5):
    p = sorted(p, key=f, reverse=True)[:2] + [m(x) for x in p]

best = max(p, key=f)
print(best, f(best))


# import random

# def fitness(x):
#     return x * x

# population = [random.randint(0,10) for _ in range(5)]

# for _ in range(5):

#     population.sort(key = fitness, reverse = True)

#     best = population[:2]

#     clones = []

#     for  b in best:
#         clones.append(b)
#         clones.append(b)

#     new_population = []

#     for c in clones:
#         mutation = random.randint(-1,1)
#         new_population.append(mutation+c)

#     population = new_population

# best_solution = max(population,key=fitness)
# print(best_solution)
# print(fitness(best_solution))
