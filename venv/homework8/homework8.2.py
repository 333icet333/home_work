import random
def rand_num():
    result = [random.randint(1, 100) for _ in range(1)]
    return result
value = rand_num()
print(value)
