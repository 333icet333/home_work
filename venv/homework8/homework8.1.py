import random
def rand_num():
    result = [random.randint(1, 100) for _ in range(1)]
    print(result)
rand_num()