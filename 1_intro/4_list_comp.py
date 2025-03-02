healthy = ["kale chips", "broccoli"]
backpack = ["pizza", "frozen custard", "apple crisp", "kale chips"]

# print(id(backpack))
# backpack[:] = [item for item in backpack if item in healthy]
# slice [:] keeps the same object id

healthy_backpack = []

for item in backpack:
    if item in healthy:
        healthy_backpack.append(item)

print(healthy_backpack)

# print(id(backpack))
print(backpack)