from collections import defaultdict

persons = [
    {"name": "John", "age": 15},
    {"name": "Jackky", "age": 41},
    {"name": "Mal", "age": 12},
    {"name": "Ray", "age": 97},
    {"name": "Janety", "age": 31}
]

age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []

for p in persons:
    name = p['name']
    age = p['age']
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)

min_age = min(age_by_names)
print('min_age:', *age_by_names[min_age])

max_len_name = max(len_name_by_names)
print('max_len_name:', *len_name_by_names[max_len_name])

print('average:', sum(ages) // len(ages))