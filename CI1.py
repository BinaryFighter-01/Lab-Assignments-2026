# Fuzzy sets
A = {'x1': 0.2, 'x2': 0.5}
B = {'x1': 0.6, 'x2': 0.3}

# Union: max(A,B)
print("Union:", {x: max(A[x], B[x]) for x in A})

# Intersection: min(A,B)
print("Intersection:", {x: min(A[x], B[x]) for x in A})

# Complement: 1 - A
print("Complement A:", {x: 1 - A[x] for x in A})

# Difference: min(A, 1-B)
print("A-B:", {x: min(A[x], 1 - B[x]) for x in A})

# Relation R (A x B): min(A(x), B(y))
R = {(x, y): min(A[x], B[y]) for x in A for y in B}

# Another set C
C = {'y1': 0.7}

# Relation S (B x C): min(B(y), C(z))
S = {(y, z): min(B[y], C[z]) for y in B for z in C}

# Max-Min Composition: max(min(R,S))
T = {(x, z): max(min(R[(x, y)], S[(y, z)]) for y in B) for x in A for z in C}

print("Composition:", T)