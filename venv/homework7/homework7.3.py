my_list = ["cat", "list", "dog", "rules", "python", "grenka"]
new_list= []
for index, item in enumerate(my_list):
    if index%2!=0:
        new_list.append(item[::-1])
    else:
        new_list.append(item)
print(new_list)
