# This can be used to transpose a 2D array

arr = [['a', 'b'], ['c', 'd'], ['e', 'f']]
transposed = zip(*arr)
print(list(transposed))
