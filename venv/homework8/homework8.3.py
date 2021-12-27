import random
def rand_num():
    result = [random.randint(1, 100) for _ in range(1)]
    print(result)
    for i in list(result):
        if i >= 50:
            print("Хорошо")
        else:
            print("Плохо")
rand_num()