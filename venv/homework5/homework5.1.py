import random

size = 20
random_size = 20
result = []
for _ in range(size):
    result.append(random.randint(1, random_size))
print(result)
for i in list(result):
    if result.count(i) > 1:
        result.remove(i)
print(result)