import copy
import random

size = 20
random_size = 20
result = []
for _ in range(size):
    result.append(random.randint(1, random_size))
print(result)

result_copy = result.copy()
print(result_copy)

