import random

size = 10
random_size = 10
result = []
for _ in range(size):
    result.append(random.randint(1, random_size))
print(result)

random_copy = result * 1

print (random_copy)




