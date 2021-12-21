import random

LIST_SIZE = 5
RANDOM_NUMBERS_SIZE = 5
numbers_list_A = []
numbers_list_B = []
for _ in range(LIST_SIZE):
    numbers_list_A.append(random.randint(1, RANDOM_NUMBERS_SIZE))
print(numbers_list_A)
for _ in range(LIST_SIZE):
    numbers_list_B.append(random.randint(1, RANDOM_NUMBERS_SIZE))
print(numbers_list_B)
dif_namber_list = []
dif_namber_list = (set(numbers_list_A).difference(numbers_list_B))
print(dif_namber_list)