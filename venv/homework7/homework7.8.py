my_str = "abcdefg"
result = []
for index, value in enumerate(my_str):
    if index % 2 == 0:
        couple = my_str[index:index+2]
        if len(couple)>1:
            result.append(couple)
        else:
            result.append(value+"_")
print("EASY", result)