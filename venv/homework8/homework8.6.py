def get_list_1(list_param):
    new_list_param = " ".join(list_param)
    new_list_param = new_list_param.upper()
    list_param = new_list_param.split(" ")
    return list_param

list_exemp = ["grenka", "hello", "world"]
value = get_list_1(list_exemp)
print(value)