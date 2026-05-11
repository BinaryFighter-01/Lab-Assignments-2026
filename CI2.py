import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


# Load data
X, y = load_iris(return_X_y=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

best_acc = 0
best = None

# Genetic Algorithm
for i in range(5):

    # Random parameters
    neurons = random.randint(5, 20)

    lr = random.uniform(0.001, 0.1)

    # Neural Network
    model = MLPClassifier(
        hidden_layer_sizes=(neurons,),
        learning_rate_init=lr,
        max_iter=300
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    acc = accuracy_score(y_test, pred)

    print(neurons, lr, acc)

    # Best solution
    if acc > best_acc:

        best_acc = acc

        best = [neurons, lr]


print("\nBest Parameters =", best)

print("Best Accuracy =", best_acc)
