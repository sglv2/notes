import random

# Random
random.seed(3)
print(random.random())
print(random.random())
print(random.randrange(1, 10))
print(random.sample(range(100), 10))

# print with separator
print(1, 2, 3, sep='|')
