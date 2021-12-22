my_str = "My long string"
l_limit = "o"
r_limit = "g"
i1 = my_str.find(l_limit)
i2 = my_str.rfind(r_limit)
sub_str = my_str[i1+1 : i2]

print(sub_str)