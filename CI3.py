import random

t = [1,0,1,1]

def f(x): return sum(x[i]==t[i] for i in range(len(t)))
def m(x): return [b if random.random()>0.3 else 1-b for b in x]

p = [[random.randint(0,1) for _ in t] for _ in range(6)]

for _ in range(5):
    p = sorted(p, key=f, reverse=True)[:2] + [m(x) for x in p]

best = max(p, key=f)
print(best, f(best))