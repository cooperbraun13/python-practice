# LIST COMPREHENSION ESSENTIALS

# expression (result) -> list or iterable its coming from -> condition to see if something is met
squares = [i ** 2 for i in range(10) if i % 2 == 0]

# for i in range(10):
    # squares.append(i ** 2)

print(squares)

