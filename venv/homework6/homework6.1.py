import random
list1 = []
for _ in range(10):
    list1.append(random.randint(1, 11))
print(list1)
print(type(list1))
tuple1 = tuple(list1)
print(tuple1)
print(type(tuple1))