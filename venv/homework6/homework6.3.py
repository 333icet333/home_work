tuple1 = (1, 2, 3, 4)
a1, b1, c1, d1 = tuple1
# print(f"a1 {a1}, b1 {b1}, c1 {c1}, d1 {d1}")
tuple2 = (3, 5, 2, 1)
a2, b2, c2, d2 = tuple2
tuple3 = (2, 2, 3, 1)
a3, b3, c3, d3 = tuple3
list1 = [(tuple1), (tuple2), (tuple3)]
list1 = [(a1 + a2 + a3), (b1 + b2 + b3), (c1 + c2 + c3), (d1 + d2 + d3)]
tuple_res = tuple(list1)
print(tuple_res)