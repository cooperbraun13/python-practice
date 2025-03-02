healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

# print(id(backpack))
backpack[:] = [item for item in backpack if item in healthy]
# slice [:] keeps the same object id

# print(id(backpack))
print(backpack)

# does same thing, just creates new variable
healthy_backpack = []

for item in backpack:
    if item in healthy:
        healthy_backpack.append(item.upper())

print(healthy_backpack)