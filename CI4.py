import random
from deap import base, creator, tools, algorithms

# 1. Fitness & Individual (ALWAYS FIRST)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

# 2. Toolbox
toolbox = base.Toolbox()

toolbox.register("attr", random.randint, 0, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, 3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 3. Fitness function
def eval(ind):
    return (ind[0]**2,)   # ALWAYS tuple

toolbox.register("evaluate", eval)

# 4. Operators
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=10, indpb=0.2)
toolbox.register("select", tools.selBest)

# 5. Run
pop = toolbox.population(n=5)
algorithms.eaSimple(pop, toolbox, cxpb=0.7, mutpb=0.2, ngen=5)

# 6. Result
best = tools.selBest(pop, 1)[0]
print(best, best.fitness.values)
