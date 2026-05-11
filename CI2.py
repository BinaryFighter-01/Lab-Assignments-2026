import warnings
warnings.filterwarnings('ignore')
import random
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier



data=load_iris()
X=data.data
y=data.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

def create_population(size):
    population=[]
    for _ in range(size):
        neurons=random.randint(5,20)
        lr=random.uniform(0.001,0.1)
        population.append([neurons,lr])
    return population


def fitness(individual):
    neurons,lr=individual
    model=MLPClassifier(hidden_layer_sizes=(neurons,),learning_rate_init=lr,max_iter=30)

    model.fit(X_train,y_train)
    predictions=model.predict(X_test)
    return accuracy_score(y_test,predictions)
    

def select(population):
    population.sort(key=fitness,reverse=True)
    return population[:2]


def crossover(parent1,parent2):
    return [parent1[0],parent2[1]]


def mutate(individual):
    if random.random()<0.3:
        individual[0]=random.randint(5,20)

    if random.random()<0.3:
        individual[1]=random.uniform(0.001,0.1)

    return individual

population=create_population(6)

for generation in range(5):
    best=select(population)
    new_population=best.copy()
    while(len(new_population)<6):
        parent1=random.choice(best)
        parent2=random.choice(best)

        child=crossover(parent1,parent2)
        child=mutate(child)
        new_population.append(child)

    population=new_population
    

best_ind=select(population)[0]
print("best_ind",best_ind)

final_model=MLPClassifier(hidden_layer_sizes=(best_ind[0],),learning_rate_init=best_ind[1],max_iter=30)


final_model.fit(X_train,y_train)
final_pred=final_model.predict(X_test)
print("Final acc:",accuracy_score(y_test,final_pred))
