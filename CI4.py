from deap import base, creator, tools, algorithms
import random

# Maximize function: f(x) = x^2
def eval_func(ind):
    return (ind[0]**2,)

# Define fitness and individual
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Gene: random number
toolbox.register("attr", random.uniform, -10, 10)

# Individual and population
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Operators
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run GA
pop = toolbox.population(n=10)
algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=5, verbose=False)

# Best result
best = tools.selBest(pop, 1)[0]
print("Best:", best, "Fitness:", best.fitness.values)