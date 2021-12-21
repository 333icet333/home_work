import random

LIST_SIZE = 5
RANDOM_NUMBERS_SIZE = 5
numbers_list_1 = []
numbers_list_2 = []
for _ in range(LIST_SIZE):
    numbers_list_1.append(random.randint(1, RANDOM_NUMBERS_SIZE))
print(numbers_list_1)
for _ in range(LIST_SIZE):
    numbers_list_2.append(random.randint(1, RANDOM_NUMBERS_SIZE))
print(numbers_list_2)
numbers_list_1 = set(numbers_list_1)
numbers_list_2 = set(numbers_list_2)
check_1 = numbers_list_1 <= numbers_list_2
check_2 = numbers_list_2 >= numbers_list_1
print(check_1)
print(check_2)