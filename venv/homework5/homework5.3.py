import random

size = 5
random_size = 5
result = []
for _ in range(size):
    result.append(random.randint(1, random_size))
print(result)


size_2 = 5
random_size_2 = 5
result_2 = []
for _ in range(size_2):
    result_2.append(random.randint(1, random_size_2))
print(result_2)


result_3=list(set(result)-set(result_2))
print (result_3)

