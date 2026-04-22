from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import random

# Load data
X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2)

# Create individual [neurons, learning_rate]
def create():
    return [random.randint(5, 50), random.uniform(0.001, 0.1)]

# Fitness = accuracy
def fit(ind):
    m = MLPClassifier(hidden_layer_sizes=(ind[0],),
                      learning_rate_init=ind[1],
                      max_iter=200)
    m.fit(Xtr, ytr)
    return m.score(Xte, yte)

# Initial population
pop = [create() for _ in range(6)]

# GA loop
for _ in range(5):
    pop = sorted(pop, key=fit, reverse=True)[:2] + \
          [create() for _ in range(4)]

# Best result
best = max(pop, key=fit)
print(best, fit(best))