import random
numbers = []
numbers_size = random.randint(10, 15)
print(numbers_size)

for _ in range(numbers_size):
    numbers.append(random.randint(10, 20))

print(numbers)
