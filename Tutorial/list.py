A = [2, 4, 1231238429, 5]

print(id(A[2]))

A.insert(1, 10)

print(id(A[3]))

print(A)

A[3] = 6

print(id(A[3]))
