l=["cat", "list", "dog", "rules", "python", "grenka"]
nl=[]
for index, item in enumerate(l):
    if index%2!=0:
        nl.append(item[::-1])
    else:
        nl.append(item)
print(nl)
